"""The noir kit: black cutout critters, lit from behind, one face engine (skia-python).

A sprite is 320 x 256; the feet touch y = 256. A critter gives its silhouette, its few
pale or red details and where its face sits; the kit draws the backlight rim, the eyes,
the mouth and the status marks, so every critter poses the same way.
Keep the top corners (x < 70 or x > 250, y < 109) free: the marks go there.
"""

import io
import re
from collections.abc import Callable
from dataclasses import dataclass, field

import skia
from PIL import Image

W, H = 320, 256
STATUSES = ("idle", "working", "blocked", "done")

INK = "#060608"  # the silhouette black
FOLD = "#1e1e24"  # faint lines inside the silhouette: coat seams, wing edges
BLOOD = "#e0303c"  # the one accent: trouble, and a few tiny details
# Status colors, matched to theme.js.
WORKING, BLOCKED, DONE, IDLE = "#f4f1e8", BLOOD, "#a8a69e", "#6e6e76"
# The backlight on the silhouette's edge, per status (the scene's light color).
RIM = {"idle": "#7a7a84", "working": "#f4f1e8", "blocked": "#ff4a52", "done": "#d8d0bc"}
# A soft halo behind the body, per status: (color, alpha, blur sigma).
HALO = {
    "idle": ("#8a8a96", 0.30, 7),
    "working": ("#f4f1e8", 0.55, 9),
    "blocked": ("#ff3040", 0.60, 9),
    "done": ("#e4dccb", 0.45, 9),
}


def color(hex_: str, alpha: float = 1.0) -> int:
    """A skia color from '#rrggbb' and an alpha in 0..1."""
    h = hex_.lstrip("#")
    return skia.Color(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), round(alpha * 255))


def paint(hex_: str, alpha: float = 1.0, stroke: float = 0, blur: float = 0, cap=skia.Paint.kRound_Cap) -> skia.Paint:
    """An anti-aliased fill paint, or a round stroke when `stroke` > 0, blurred by `blur` sigma."""
    p = skia.Paint(AntiAlias=True, Color=color(hex_, alpha))
    if stroke:
        p.setStyle(skia.Paint.kStroke_Style)
        p.setStrokeWidth(stroke)
        p.setStrokeCap(cap)
        p.setStrokeJoin(skia.Paint.kRound_Join)
    if blur:
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, blur))
    return p


# ---- path helpers -------------------------------------------------------------------


def poly(*pts: tuple[float, float]) -> skia.Path:
    """A closed polygon."""
    p = skia.Path()
    p.addPoly([skia.Point(*q) for q in pts], True)
    return p


def oval(cx: float, cy: float, rx: float, ry: float) -> skia.Path:
    """An ellipse by center and radii."""
    p = skia.Path()
    p.addOval(skia.Rect.MakeLTRB(cx - rx, cy - ry, cx + rx, cy + ry))
    return p


def stroked(path: skia.Path, width: float) -> skia.Path:
    """The outline of a round-capped stroke along `path`, as a fill path."""
    out = skia.Path()
    paint("#000000", stroke=width).getFillPath(path, out)
    return out


def union(*paths: skia.Path) -> skia.Path:
    """All the paths merged into one shape."""
    out = paths[0]
    for p in paths[1:]:
        out = skia.Op(out, p, skia.PathOp.kUnion_PathOp)
    return out


def cut(a: skia.Path, b: skia.Path) -> skia.Path:
    """`a` with `b` cut out of it."""
    return skia.Op(a, b, skia.PathOp.kDifference_PathOp)


def svgpath(d: str) -> skia.Path:
    """A path from absolute SVG path data: M, L, Q, C and Z (a command may repeat its numbers)."""
    p, arity = skia.Path(), {"M": 2, "L": 2, "Q": 4, "C": 6, "Z": 0}
    for cmd, args in re.findall(r"([MLQCZ])([^MLQCZ]*)", d):
        nums = [float(n) for n in re.findall(r"-?\d*\.?\d+", args)]
        if cmd == "Z":
            p.close()
            continue
        for i in range(0, len(nums), arity[cmd]):
            n = nums[i : i + arity[cmd]]
            if cmd == "M":
                p.moveTo(*n) if i == 0 else p.lineTo(*n)
            elif cmd == "L":
                p.lineTo(*n)
            elif cmd == "Q":
                p.quadTo(*n)
            else:
                p.cubicTo(*n)
    return p


def to_pil(surface: skia.Surface) -> Image.Image:
    """A PIL RGBA image of a skia surface, unpremultiplied."""
    arr = surface.makeImageSnapshot().toarray(
        colorType=skia.ColorType.kRGBA_8888_ColorType, alphaType=skia.AlphaType.kUnpremul_AlphaType
    )
    return Image.fromarray(arr, "RGBA")


def png(im: Image.Image) -> bytes:
    """PNG bytes of an image, compressed as small as Pillow goes."""
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()


# ---- the critter --------------------------------------------------------------------


@dataclass
class Critter:
    shape: skia.Path  # the whole black cutout, hat and coat included
    eyes: list[tuple[float, float]]  # eye centers
    mouth: tuple[float, float]  # mouth center
    eye: float = 8  # eye radius; 7 to 11 reads at the small size
    pupil: str = "round"  # "round" or "slit" (cats)
    folds: list[skia.Path] = field(default_factory=list)  # faint seams drawn inside the cutout
    lines: list[tuple[skia.Path, float]] = field(default_factory=list)  # thin ink strokes past the edge: whiskers
    details: Callable[[skia.Canvas, str], None] | None = None  # pale hat, red tie, lens: drawn on the body


def _eye_open(cv: skia.Canvas, x: float, y: float, r: float, hex_: str, pupil: str, look: float) -> None:
    """A glowing open eye with a dark pupil, looking right by `look`."""
    cv.drawPath(oval(x, y, r * 1.5, r * 1.4), paint(hex_, 0.55, blur=r * 0.6))
    cv.drawPath(oval(x, y, r * 0.9, r), paint(hex_))
    if pupil == "slit":
        cv.drawPath(oval(x + look, y, r * 0.22, r * 0.8), paint(INK))
    else:
        cv.drawPath(oval(x + look, y + r * 0.1, r * 0.42, r * 0.48), paint(INK))


def face(cv: skia.Canvas, c: Critter, status: str) -> None:
    """Eyes and mouth for one status, on top of the black body."""
    r, (mx, my) = c.eye, c.mouth
    for x, y in c.eyes:
        if status == "idle":  # shut: a heavy flat lid with a droop at the ends
            lid = svgpath(f"M{x - r} {y - 1}Q{x} {y + r * 0.55} {x + r} {y - 1}")
            cv.drawPath(lid, paint("#9a9aa4", stroke=max(2.5, r * 0.32)))
        elif status == "working":  # wide open, bright, looking toward the clue
            _eye_open(cv, x, y, r, WORKING, c.pupil, r * 0.25)
        elif status == "blocked":  # red and narrowed: the inner top corner cut by a frown
            side = -1 if x < mx else 1
            cv.save()
            brow = poly((x - r * 1.6, y - r * 1.6), (x + r * 1.6, y - r * 1.6),
                        (x + r * 1.6, y - r * 0.15 * side - r * 0.25), (x - r * 1.6, y + r * 0.15 * side - r * 0.25))
            if len(c.eyes) == 1:  # a lone profile eye frowns toward the beak
                brow = poly((x - r * 1.6, y - r * 1.6), (x + r * 1.6, y - r * 1.6), (x + r * 1.6, y - r * 0.05), (x - r * 1.6, y - r * 0.55))
            cv.clipPath(brow, skia.ClipOp.kDifference, True)
            cv.drawPath(oval(x, y, r * 1.6, r * 1.5), paint(BLOOD, 0.6, blur=r * 0.7))
            cv.drawPath(oval(x, y, r * 0.95, r), paint(BLOOD))
            cv.drawPath(oval(x, y + r * 0.15, r * 0.3, r * 0.35), paint("#ffd0d0"))
            cv.restore()
        else:  # done: happy arcs ^ ^
            arc = svgpath(f"M{x - r} {y + r * 0.45}Q{x} {y - r * 1.15} {x + r} {y + r * 0.45}")
            cv.drawPath(arc, paint("#efe9da", stroke=max(3, r * 0.42)))
    if status == "blocked":  # a tight wavy line
        w = svgpath(f"M{mx - 7} {my + 1}Q{mx - 3.5} {my - 3} {mx} {my + 1}Q{mx + 3.5} {my + 5} {mx + 7} {my + 1}")
        cv.drawPath(w, paint("#ff8088", stroke=2.6))
    elif status == "done":  # a small smile
        s = svgpath(f"M{mx - 8} {my - 2}Q{mx} {my + 6} {mx + 8} {my - 2}")
        cv.drawPath(s, paint("#efe9da", stroke=3))


# ---- status marks ---------------------------------------------------------------------


def _outlined(cv: skia.Canvas, path: skia.Path, hex_: str, width: float, fill: bool = False) -> None:
    """A mark stroke (or fill) in `hex_` with a thick black edge, so it reads on any scene."""
    if fill:
        cv.drawPath(path, paint(INK, stroke=width))
        cv.drawPath(path, paint(hex_))
    else:
        cv.drawPath(path, paint(INK, stroke=width + 7))
        cv.drawPath(path, paint(hex_, stroke=width))


def _spark(cx: float, cy: float, r: float) -> skia.Path:
    q = r * 0.24
    return poly((cx, cy - r), (cx + q, cy - q), (cx + r, cy), (cx + q, cy + q),
                (cx, cy + r), (cx - q, cy + q), (cx - r, cy), (cx - q, cy - q))


def marks(cv: skia.Canvas, status: str) -> None:
    """Status marks in the top corners: z, ? , ! and a raindrop, a check and a spark."""
    if status == "idle":
        _outlined(cv, svgpath("M266 44L284 44L266 64L284 64"), "#b4b4bc", 5)
        _outlined(cv, svgpath("M290 18L302 18L290 31L302 31"), "#8e8e98", 4)
    elif status == "working":
        q = svgpath("M22 34C22 14 56 12 56 32C56 46 39 46 39 62")
        _outlined(cv, q, WORKING, 8)
        _outlined(cv, oval(39, 82, 6, 6), WORKING, 7, fill=True)
    elif status == "blocked":
        bang = svgpath("M33 16L49 16L44 64L38 64Z")
        cv.drawPath(bang, paint(BLOOD, 0.6, blur=8))
        _outlined(cv, bang, BLOOD, 7, fill=True)
        _outlined(cv, oval(41, 82, 7, 7), BLOOD, 7, fill=True)
        cv.drawPath(svgpath("M39 21L44 21L41 50Z"), paint("#ff9aa0"))
        drop = svgpath("M282 20Q268 44 268 54C268 73 296 73 296 54Q296 44 282 20Z")
        _outlined(cv, drop, "#cfd4da", 7, fill=True)
        cv.drawPath(oval(276, 52, 3, 5), paint("#ffffff"))
    else:
        tick = svgpath("M20 44L36 62L62 24")
        _outlined(cv, tick, "#efe9da", 9)
        sp = _spark(282, 40, 20)
        cv.drawPath(sp, paint("#fff6e0", 0.5, blur=6))
        _outlined(cv, sp, "#fbf6ea", 6, fill=True)


def sprite(c: Critter, status: str) -> bytes:
    """One critter's PNG for one status: halo, rim light, black body, details, face, marks."""
    surf = skia.Surface(W, H)
    cv = surf.getCanvas()
    cv.clear(skia.ColorTRANSPARENT)
    hue, alpha, sigma = HALO[status]
    cv.drawPath(c.shape, paint(hue, alpha, blur=sigma))
    rim = RIM[status]
    for dx, dy in ((-2.5, -2), (2.5, -2), (0, -3)):
        cv.save()
        cv.translate(dx, dy)
        cv.drawPath(c.shape, paint(rim))
        cv.restore()
    cv.drawPath(c.shape, paint(INK))
    for line, wd in c.lines:
        cv.drawPath(line, paint(INK, stroke=wd))
    for f in c.folds:
        cv.drawPath(f, paint(FOLD, stroke=2.5))
    if c.details:
        c.details(cv, status)
    face(cv, c, status)
    marks(cv, status)
    return png(to_pil(surf))
