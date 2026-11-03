"""The deepsea drawing kit: soft gel critters, lit from inside, drawn with skia-python.

A sprite is drawn in a 100 x 80 box and saved as a 320 x 256 PNG; the feet touch y = 80.
A critter is a list of parts and where its face sits; the kit draws every part as
see-through gel (a soft halo, a radial gradient with a bright core, an inner rim glow
and a shine, no outline), then the glowing spots, the face and the status marks, so
every critter poses the same way.
Keep the top corners (x < 22 or x > 78, y < 34) free: the marks go there.
"""

import io
from dataclasses import dataclass, field

import imagequant
import skia
from PIL import Image

from .paths import path

W, H = 100, 80
PX = 3.2  # pixels per box unit in a sprite
STATUSES = ("idle", "working", "blocked", "done")

BG = "#070b18"  # theme.js colors.bg
INK = "#1a1038"  # the face
WHITE = "#ffffff"
# Mark colors, matched to theme.js status colors.
DIVE, SOS, DOCK, DRIFT = "#3ff0ff", "#ff4f8b", "#6bffb0", "#8a96b8"
BUBBLE = "#9fe8ff"
STATUS = {"working": DIVE, "blocked": SOS, "done": DOCK, "idle": DRIFT}


# ---- colors and paints


def rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def mix(a: str, b: str, t: float) -> str:
    """Color a moved toward b by t (0 gives a, 1 gives b)."""
    return "#%02x%02x%02x" % tuple(round(x + (y - x) * t) for x, y in zip(rgb(a), rgb(b)))


def color(h: str, alpha: float = 1.0) -> int:
    return skia.ColorSetARGB(round(max(0, min(1, alpha)) * 255), *rgb(h))


def fill(h: str, alpha: float = 1.0, blur: float = 0) -> skia.Paint:
    """A fill paint; `blur` softens it into a glow."""
    p = skia.Paint(AntiAlias=True, Color=color(h, alpha))
    if blur:
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, blur))
    return p


def stroke(h: str, width: float, alpha: float = 1.0, blur: float = 0) -> skia.Paint:
    """A round line paint."""
    p = fill(h, alpha, blur)
    p.setStyle(skia.Paint.kStroke_Style)
    p.setStrokeWidth(width)
    p.setStrokeCap(skia.Paint.kRound_Cap)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    return p


def radial(cx: float, cy: float, r: float, stops: list[tuple[float, str, float]]) -> skia.Paint:
    """A paint with a radial gradient; stops are (offset, color, alpha)."""
    shader = skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [color(c, a) for _, c, a in stops], [s for s, _, _ in stops])
    return skia.Paint(AntiAlias=True, Shader=shader)


def linear(x0: float, y0: float, x1: float, y1: float, stops: list[tuple[float, str, float]], blur: float = 0) -> skia.Paint:
    """A paint with a straight gradient from (x0, y0) to (x1, y1)."""
    shader = skia.GradientShader.MakeLinear(
        [skia.Point(x0, y0), skia.Point(x1, y1)], [color(c, a) for _, c, a in stops], [s for s, _, _ in stops]
    )
    p = skia.Paint(AntiAlias=True, Shader=shader)
    if blur:
        p.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, blur))
    return p


def outline(d: str, width: float) -> skia.Path:
    """A thick round line as a closed shape."""
    out = skia.Path()
    stroke(WHITE, width).getFillPath(path(d), out)
    return out


def canvas(w: float, h: float, px: float) -> tuple[skia.Surface, skia.Canvas]:
    """A clear surface that draws in box units, `px` pixels per unit."""
    surface = skia.Surface(round(w * px), round(h * px))
    c = surface.getCanvas()
    c.clear(skia.ColorTRANSPARENT)
    c.scale(px, px)
    return surface, c


def png(surface: skia.Surface) -> bytes:
    """The surface as small PNG bytes: 256 dithered colors (libimagequant keeps the soft
    gradients smooth), saved by Pillow at full effort. About a quarter of the full size."""
    image = Image.open(io.BytesIO(bytes(surface.makeImageSnapshot().encodeToData()))).convert("RGBA")
    out = io.BytesIO()
    imagequant.quantize_pil_image(image, dithering_level=1.0, max_colors=256).save(out, "PNG", optimize=True)
    return out.getvalue()


# ---- gel


def gel(c: skia.Canvas, shape: skia.Path, col: str, strong: float = 1.0) -> None:
    """One see-through shape: a halo, a gradient body, an inner rim glow and a shine."""
    b = shape.getBounds()
    cx, cy, r = b.centerX(), b.centerY() - b.height() * 0.1, max(b.width(), b.height()) * 0.62
    c.drawPath(shape, fill(col, 0.35 * strong, blur=3.2))
    c.drawPath(shape, radial(cx, cy, r, [
        (0, mix(col, WHITE, 0.55), 0.92 * strong), (0.55, col, 0.74 * strong), (1, mix(col, BG, 0.35), 0.5 * strong)]))
    c.save()
    c.clipPath(shape, doAntiAlias=True)
    c.drawPath(shape, stroke(mix(col, WHITE, 0.6), 2.2, 0.55 * strong, blur=1.2))
    sx, sw, sh = b.left() + b.width() * 0.22, min(b.width() * 0.33, 16), min(b.height() * 0.22, 9)
    c.drawOval(skia.Rect(sx, b.top() + 1.2, sx + sw, b.top() + 1.2 + sh), fill(WHITE, 0.42 * strong, blur=1.4))
    c.restore()


def strand(c: skia.Canvas, d: str, col: str, width: float) -> None:
    """A thin see-through line: a glow and a lighter core. At least 2 wide, so it reads small."""
    p, width = path(d), max(width, 2)
    c.drawPath(p, stroke(col, width * 2.4, 0.38, blur=1.4))
    c.drawPath(p, stroke(mix(col, WHITE, 0.3), width, 0.85))
    c.drawPath(p, stroke(WHITE, width * 0.35, 0.35))


def glow(c: skia.Canvas, x: float, y: float, r: float, col: str, bright: float = 1.0) -> None:
    """A glowing dot: a photophore, a lure, a spark."""
    c.drawCircle(x, y, r * 3.2, fill(col, 0.4 * bright, blur=r * 1.8))
    c.drawCircle(x, y, r, fill(mix(col, WHITE, 0.6), 0.95 * bright, blur=r * 0.25))


# ---- critters


@dataclass
class Part:
    d: str
    kind: str = "gel"  # gel: a closed shape; limb: a thick line drawn as gel; strand: a thin glowing line;
    # flat: a plain fill (a mouth, a shadow); line: a plain line on top (stripes, ridges)
    tone: str = "body"  # a key of the critter's colors
    width: float = 2  # limb, strand and line thickness
    alpha: float = 1.0


@dataclass
class Critter:
    parts: list[Part]  # back to front; the gel and limb parts in tone "body" melt into one shape
    colors: dict[str, str]  # tone -> color; "light" lights the spots and the lure
    eyes: list[tuple[float, float]]  # eye centers: one for a side view, two for a front view
    mouth: tuple[float, float] | None = None
    eye: float = 3.4  # eye radius
    spots: list[tuple[float, float, float]] = field(default_factory=list)  # glowing photophores (x, y, r)
    lure: tuple[float, float, float] | None = None  # a light that burns bright while working
    over: list[Part] = field(default_factory=list)  # parts drawn over the face


def _body_shape(cr: Critter) -> tuple[skia.Path | None, int]:
    """The body-tone gel and limb parts as one shape, and the index of the last of them."""
    merged, last = None, -1
    for i, part in enumerate(cr.parts):
        if part.tone == "body" and part.kind in ("gel", "limb"):
            shape = outline(part.d, part.width) if part.kind == "limb" else path(part.d)
            merged = shape if merged is None else skia.Op(merged, shape, skia.PathOp.kUnion_PathOp)
            last = i
    return merged, last


def draw_part(c: skia.Canvas, part: Part, col: str) -> None:
    if part.kind == "gel":
        gel(c, path(part.d), col, part.alpha)
    elif part.kind == "limb":
        gel(c, outline(part.d, part.width), col, part.alpha)
    elif part.kind == "strand":
        strand(c, part.d, col, part.width)
    elif part.kind == "flat":
        c.drawPath(path(part.d), fill(col, part.alpha))
    else:
        c.drawPath(path(part.d), stroke(col, part.width, part.alpha))


def body(c: skia.Canvas, cr: Critter, status: str) -> None:
    merged, last = _body_shape(cr)
    for i, part in enumerate(cr.parts):
        if part.tone == "body" and part.kind in ("gel", "limb"):
            if i == last:
                gel(c, merged, cr.colors["body"])
            continue
        draw_part(c, part, cr.colors[part.tone])
    lit = {"working": 1.0, "idle": 0.4}.get(status, 0.6)
    for x, y, r in cr.spots:
        glow(c, x, y, r * 0.8, cr.colors["light"], lit)
    if cr.lure:
        x, y, r = cr.lure
        on = status == "working"
        c.drawCircle(x, y, r * (2.2 if on else 1.7), fill(cr.colors["light"], 0.55 if on else 0.3, blur=r * 0.9))
        c.drawCircle(x, y, r, fill(mix(cr.colors["light"], WHITE, 0.5), 0.95 if on else 0.6))


def face(c: skia.Canvas, cr: Critter, status: str) -> None:
    r = cr.eye
    for i, (x, y) in enumerate(cr.eyes):
        if status == "idle":  # shut, sleepy
            c.drawPath(path(f"M{x - r} {y}Q{x} {y + r} {x + r} {y}"), stroke(INK, 1.4, 0.85))
        elif status == "done":  # happy arcs
            c.drawPath(path(f"M{x - r} {y + r * 0.4}Q{x} {y - r * 1.2} {x + r} {y + r * 0.4}"), stroke(INK, 1.5, 0.9))
        elif status == "blocked":  # glowing red eyes under a cross brow
            c.drawCircle(x, y, r * 1.6, fill(SOS, 0.6, blur=r * 0.8))
            c.drawCircle(x, y, r * 0.9, fill(INK, 0.9))
            c.drawCircle(x, y, r * 0.62, fill(SOS))
            c.drawCircle(x - r * 0.25, y - r * 0.25, r * 0.22, fill(WHITE))
            tilt = 1 if (len(cr.eyes) == 1 or i == 0) else -1
            c.drawPath(path(f"M{x - r} {y - r * 1.5 - tilt * 1.2}L{x + r} {y - r * 1.5 + tilt * 1.2}"), stroke(INK, 1.3, 0.85))
        else:  # open, with a catchlight
            c.drawOval(skia.Rect(x - r * 0.75, y - r * 0.95, x + r * 0.75, y + r * 0.95), fill(INK, 0.92))
            c.drawCircle(x - r * 0.25, y - r * 0.35, r * 0.3, fill(WHITE))
    if not cr.mouth:
        return
    mx, my = cr.mouth
    if status == "done":  # an open smile and blush
        c.drawPath(path(f"M{mx - 4} {my - 1}Q{mx} {my + 5} {mx + 4} {my - 1}Z"), fill(INK, 0.85))
        for x, y in cr.eyes[:1] + cr.eyes[-1:]:
            dx = -r * 0.9 if x < mx else r * 0.9
            c.drawOval(skia.Rect(x + dx - 2.8, y + r * 1.6 - 1.4, x + dx + 2.8, y + r * 1.6 + 1.4), fill(SOS, 0.5, blur=0.8))
        return
    d = {
        "idle": f"M{mx - 2.2} {my}L{mx + 2.2} {my}",
        "working": f"M{mx - 3} {my - 0.6}Q{mx} {my + 2.4} {mx + 3} {my - 0.6}",
        "blocked": f"M{mx - 3.6} {my + 0.8}Q{mx - 1.8} {my - 1.4} {mx} {my + 0.8}Q{mx + 1.8} {my + 3} {mx + 3.6} {my + 0.8}",
    }[status]
    c.drawPath(path(d), stroke(INK, 1.3, 0.85))


# ---- status marks, in the top corners

SONAR = ["M8 10Q12 15.5 8 21", "M12 7Q18 15.5 12 24", "M16 4Q24 15.5 16 27"]  # working: ))) pings
BANG, BANG_DOT = "M11 8L11 18", (11, 24.5, 2.1)  # blocked: "!"
CHECK = "M5 16L10.5 22L20 8"  # done
BUBBLES = [(88, 15, 6), (81, 27, 2.6)]  # blocked: a worried bubble
TWINKLE = (88, 11, 5)  # working and done


def mark_line(c: skia.Canvas, d: str, col: str, w: float) -> None:
    p = path(d)
    c.drawPath(p, stroke(col, w * 2.2, 0.45, blur=w * 0.8))
    c.drawPath(p, stroke(mix(col, WHITE, 0.25), w, 0.95))
    c.drawPath(p, stroke(WHITE, w * 0.35, 0.6))


def sparkle(c: skia.Canvas, x: float, y: float, r: float, col: str) -> None:
    c.drawCircle(x, y, r * 1.1, fill(col, 0.4, blur=r * 0.7))
    q = r * 0.09
    c.drawPath(path(f"M{x} {y - r}Q{x + q} {y - q} {x + r} {y}Q{x + q} {y + q} {x} {y + r}"
                    f"Q{x - q} {y + q} {x - r} {y}Q{x - q} {y - q} {x} {y - r}Z"), fill(mix(col, WHITE, 0.6)))


def bubble(c: skia.Canvas, x: float, y: float, r: float) -> None:
    c.drawCircle(x, y, r, radial(x - r * 0.3, y - r * 0.3, r * 1.3, [(0, WHITE, 0.15), (0.7, BUBBLE, 0.25), (1, BUBBLE, 0.8)]))
    c.drawCircle(x - r * 0.35, y - r * 0.35, r * 0.28, fill(WHITE, 0.9, blur=0.3))


def marks(c: skia.Canvas, status: str) -> None:
    """Sonar pings and a sparkle (working), a "!" and a bubble (blocked), a check and a sparkle (done)."""
    col = STATUS[status]
    if status == "working":
        for i, d in enumerate(SONAR):
            c.drawPath(path(d), stroke(col, 1.8, 0.85 - i * 0.22, blur=0.5))
        sparkle(c, *TWINKLE, col)
    elif status == "blocked":
        mark_line(c, BANG, col, 3)
        glow(c, *BANG_DOT, col)
        for b in BUBBLES:
            bubble(c, *b)
    elif status == "done":
        mark_line(c, CHECK, col, 2.6)
        sparkle(c, *TWINKLE, col)


def sprite(cr: Critter, status: str) -> bytes:
    """One critter's PNG for one status."""
    surface, c = canvas(W, H, PX)
    body(c, cr, status)
    face(c, cr, status)
    for part in cr.over:
        draw_part(c, part, cr.colors[part.tone])
    marks(c, status)
    return png(surface)
