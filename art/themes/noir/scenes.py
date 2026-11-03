"""The noir scenes: a detective's office at night, one tall window with venetian blinds
behind the critter, so its black cutout reads against the light in every status.

576 x 480, opaque; the feet line is y = 385. The light through the window sets the
status: a dim streetlamp in the fog (idle), hard white light (working), a red neon sign
in the rain (blocked), soft warm gray (done).
"""

import math
from dataclasses import dataclass

import skia
from PIL import Image

from .kit import BLOOD, color, oval, paint, png, poly, svgpath, to_pil, union

W, H, FLOOR = 576, 480, 385
GLASS = skia.Rect.MakeLTRB(150, 46, 426, 352)  # the window opening, behind the critter


@dataclass
class Light:
    wall: tuple[str, str]  # wall gradient, top to bottom
    glass: tuple[str, str]  # window light, center to edge
    slat: str  # blind slat body
    slat_hi: str  # lit top edge of a slat
    stripe: tuple[str, float]  # light stripes cast on the floor
    floor: str


LIGHTS = {
    "idle": Light(("#0b0b0e", "#141419"), ("#6a6a78", "#22222a"), "#18181e", "#3c3c46", ("#56566a", 0.35), "#0c0c0f"),
    "working": Light(("#1c1c1f", "#26262a"), ("#fffdf6", "#aaa69a"), "#55534e", "#f4f1e8", ("#f4f1e8", 0.55), "#17171a"),
    "blocked": Light(("#16070a", "#1e0a0d"), ("#ff6a70", "#5c0c14"), "#2c0a0e", "#c42a34", ("#e0303c", 0.45), "#120507"),
    "done": Light(("#1c1915", "#24201b"), ("#e2d2b2", "#5e574a"), "#3a352d", "#c4b494", ("#d6c6a4", 0.32), "#16130f"),
}


def _linear(top: str, bottom: str, y0: float, y1: float) -> skia.Paint:
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear([skia.Point(0, y0), skia.Point(0, y1)], [color(top), color(bottom)]))
    return p


def _radial(cx: float, cy: float, r: float, inner: str, outer: str, a0: float = 1, a1: float = 1) -> skia.Paint:
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeRadial(skia.Point(cx, cy), r, [color(inner, a0), color(outer, a1)]))
    return p


def _city(cv: skia.Canvas, alpha: float, lit: str | None = None) -> None:
    """Far buildings behind the glass, a few windows lit in `lit`."""
    city = paint("#000000", alpha)
    for x, top in ((150, 250), (192, 214), (236, 276), (300, 232), (352, 262), (392, 204)):
        cv.drawRect(skia.Rect.MakeLTRB(x, top, x + 40, 352), city)
        if lit:
            for i in range(3):
                wx, wy = x + 8 + (i * 13) % 26, top + 14 + i * 22
                cv.drawRect(skia.Rect.MakeLTRB(wx, wy, wx + 5, wy + 7), paint(lit, 0.7))


# The neon letters of the hotel sign, as tube strokes in a 26 x 36 box.
_LETTERS = {
    "H": "M0 0L0 36M26 0L26 36M0 18L26 18",
    "O": "M13 0C30 0 30 36 13 36C-4 36 -4 0 13 0Z",
    "T": "M0 0L26 0M13 0L13 36",
    "E": "M26 0L0 0L0 36L26 36M0 18L20 18",
    "L": "M0 0L0 36L26 36",
}


def _neon(cv: skia.Canvas, word: str, x: float, y: float) -> None:
    """A neon sign on a dark board: glowing red tubes with a hot pale core."""
    width = len(word) * 38 - 12
    cv.drawPath(oval(x + width / 2, y + 18, width * 0.9, 70), paint("#ff2030", 0.45, blur=28))
    board = skia.Rect.MakeLTRB(x - 14, y - 12, x + width + 14, y + 48)
    cv.drawRoundRect(board, 6, 6, paint("#0c0405"))
    cv.drawRoundRect(board, 6, 6, paint("#5a1016", stroke=2))
    for i, ch in enumerate(word):
        p = svgpath(_LETTERS[ch])
        p.offset(x + i * 38, y)
        cv.drawPath(p, paint("#ff2a3a", 0.9, stroke=9, blur=5))
        cv.drawPath(p, paint("#ff4a56", stroke=5))
        cv.drawPath(p, paint("#ffd0d2", stroke=2))


def _rain(cv: skia.Canvas, hue: str, alpha: float) -> None:
    rain = paint(hue, alpha, stroke=1.4)
    for i in range(70):
        x = 150 + (i * 53) % 290
        y = 46 + (i * 97) % 300
        cv.drawLine(x, y, x - 6, y + 22, rain)


def _outside(cv: skia.Canvas, status: str, lt: Light) -> None:
    """What the window shows, behind the blinds."""
    cv.drawRect(GLASS, _radial(288, 210, 230, *lt.glass))
    if status == "idle":  # a streetlamp in the fog, mostly hidden by shut blinds
        _city(cv, 0.35)
        cv.drawPath(svgpath("M392 352L392 92Q392 76 376 76L360 76"), paint("#0a0a0d", stroke=6))
        cone = skia.Paint(AntiAlias=True)
        cone.setShader(skia.GradientShader.MakeLinear(
            [skia.Point(0, 84), skia.Point(0, 352)], [color("#c8c8d4", 0.55), color("#8a8a98", 0.0)]))
        cv.drawPath(poly((354, 84), (368, 84), (430, 352), (250, 352)), cone)
        cv.drawPath(oval(361, 86, 16, 8), paint("#e4e4ec", 0.8, blur=6))
    elif status == "working":  # hard white light from a searchlight on the street
        _city(cv, 0.18)
        cv.drawPath(oval(288, 190, 120, 110), paint("#ffffff", 0.7, blur=40))
    elif status == "blocked":  # blinds up: a red HOTEL sign buzzing in the rain
        _city(cv, 0.55, "#ff6a70")
        _neon(cv, "HOTEL", 199, 92)
        _rain(cv, "#ffc0c4", 0.35)
    else:  # blinds half up: dawn over the skyline, a low sun
        sky = skia.Paint(AntiAlias=True)
        sky.setShader(skia.GradientShader.MakeLinear(
            [skia.Point(0, 150), skia.Point(0, 352)], [color("#6e675c"), color("#f0e2c4")]))
        cv.drawRect(GLASS, sky)
        cv.drawPath(oval(288, 330, 70, 70), paint("#fff4dc", 0.9, blur=18))
        cv.drawPath(oval(288, 330, 40, 40), paint("#fffaf0"))
        _city(cv, 0.75)


def _blinds(cv: skia.Canvas, lt: Light, status: str) -> None:
    """Venetian blind slats: shut for idle, wide open for working, pulled up for
    blocked (bunched at the top), half up for done."""
    pitch = 17
    body, bottom = {"idle": (15, GLASS.bottom()), "working": (6, GLASS.bottom()),
                    "blocked": (4, GLASS.top() + 30), "done": (9, 196)}[status]
    if status == "blocked":
        pitch = 6
    y = GLASS.top() + 3
    while y < bottom:
        cv.drawRect(skia.Rect.MakeLTRB(GLASS.left(), y, GLASS.right(), min(y + body, bottom)), paint(lt.slat))
        cv.drawRect(skia.Rect.MakeLTRB(GLASS.left(), y, GLASS.right(), y + 1.6), paint(lt.slat_hi, 0.8))
        y += pitch
    rail = skia.Rect.MakeLTRB(GLASS.left() - 2, bottom, GLASS.right() + 2, bottom + 6)
    cv.drawRect(rail, paint("#0a0a0c"))  # the bottom rail
    cord = paint("#0a0a0c", stroke=1.5)
    cv.drawLine(176, GLASS.top(), 176, bottom + 40, cord)
    cv.drawPath(oval(176, bottom + 44, 3, 5), paint("#0a0a0c"))


def _floor(cv: skia.Canvas, lt: Light, status: str) -> None:
    """The floor, with the blinds' light stripes thrown across it, and a pool of light."""
    cv.drawRect(skia.Rect.MakeLTRB(0, FLOOR, W, H), paint(lt.floor))
    hue, a = lt.stripe
    cv.save()
    cv.clipRect(skia.Rect.MakeLTRB(0, FLOOR, W, H))
    for i in range(7):
        y0 = FLOOR + 4 + i * 13
        y1 = y0 + 6 + i * 0.6
        spread = 1 + i * 0.12
        cv.drawPath(poly((288 - 150 * spread - 30, y0), (288 + 150 * spread - 30, y0),
                         (288 + 160 * spread - 20, y1), (288 - 160 * spread - 20, y1)),
                    paint(hue, a * (1 - i * 0.1), blur=1.2 if status != "done" else 2.5))
    cv.restore()
    cv.drawRect(skia.Rect.MakeLTRB(0, FLOOR - 1, W, FLOOR + 1.5), paint("#000000", 0.6))


def _room(cv: skia.Canvas, lt: Light, status: str) -> None:
    """Frame, sill, a coat rack and a desk edge: black shapes at the sides."""
    frame = paint("#050506")
    cv.drawRect(GLASS.makeOutset(10, 10), paint("#050506", stroke=12, cap=skia.Paint.kButt_Cap))
    cv.drawRect(skia.Rect.MakeLTRB(132, 356, 444, 368), frame)
    cv.drawRect(skia.Rect.MakeLTRB(132, 356, 444, 358), paint(lt.slat_hi, 0.6))
    # a backlight haze below the sill, so the critter's lower half still reads
    cv.drawPath(oval(288, 372, 150, 26), paint(lt.glass[0], 0.28 if status != "idle" else 0.22, blur=22))
    # coat rack, left
    rack = paint("#040405")
    cv.drawRect(skia.Rect.MakeLTRB(58, 120, 64, FLOOR), rack)
    cv.drawPath(svgpath("M40 FLOORL61 368L82 FLOOR".replace("FLOOR", str(FLOOR))), paint("#040405", stroke=5))
    cv.drawPath(svgpath("M61 132L40 118M61 132L82 118M61 150L44 140"), paint("#040405", stroke=4))
    cv.drawPath(svgpath("M30 128Q42 108 54 120L60 160L42 200Q30 170 30 128Z"), rack)  # a hung coat
    cv.drawPath(oval(72, 112, 18, 5), rack)  # a hat on the hook
    cv.drawPath(svgpath("M62 112L64 96Q72 90 80 96L82 112Z"), rack)
    # desk corner, right
    cv.drawRect(skia.Rect.MakeLTRB(470, 300, W, 312), rack)
    cv.drawRect(skia.Rect.MakeLTRB(484, 312, 496, FLOOR), rack)
    cv.drawPath(svgpath("M500 300L506 262L532 262L540 300Z"), rack)  # a phone
    cv.drawPath(svgpath("M496 258Q520 242 546 258"), paint("#040405", stroke=7))
    cv.drawRect(skia.Rect.MakeLTRB(470, 300, W, 301.5), paint(lt.slat_hi, 0.35))


def _smoke(cv: skia.Canvas, status: str) -> None:
    """Thin cigarette smoke curling up from the desk."""
    if status not in ("working", "done"):
        return
    for k, a in ((0, 0.22), (1, 0.14)):
        pts = [f"{524 + 10 * math.sin(i * 0.9 + k) + k * 8} {256 - i * 22}" for i in range(9)]
        cv.drawPath(svgpath("M" + "L".join(pts)), paint("#d8d4c8", a, stroke=5 - k * 2, blur=3))


def _vignette(cv: skia.Canvas) -> None:
    cv.drawRect(skia.Rect.MakeWH(W, H), _radial(288, 230, 380, "#000000", "#000000", 0.0, 0.75))


def scene(status: str) -> Image.Image:
    """The office for one status."""
    lt = LIGHTS[status]
    surf = skia.Surface(W, H)
    cv = surf.getCanvas()
    cv.drawRect(skia.Rect.MakeWH(W, FLOOR), _linear(*lt.wall, 0, FLOOR))
    # light spilling from the window onto the wall around it
    cv.drawPath(oval(288, 200, 230, 210), paint(lt.glass[0], 0.10 if status == "idle" else 0.16, blur=40))
    cv.save()
    cv.clipRect(GLASS)
    _outside(cv, status, lt)
    _blinds(cv, lt, status)
    cv.restore()
    _floor(cv, lt, status)
    _room(cv, lt, status)
    _smoke(cv, status)
    _vignette(cv)
    return to_pil(surf).convert("RGBA")


# ---- icons ----------------------------------------------------------------------------

# The light each machine icon shows, from the machine scenes in theme.js: (glow, frame).
_TONES = {
    "office": ("#c8b896", "#4e473a"), "alley": ("#9fb0bc", "#3a4550"),
    "precinct": ("#bdbdc4", "#46464e"), "records": ("#a4b4a6", "#3c4840"),
    **{s: (lt.glass[0], lt.slat) for s, lt in LIGHTS.items()},
}


def machine(glow: str, frame: str) -> bytes:
    """A machine: a lit window with blinds, 60 x 44 (the mod shows it at 15 x 11)."""
    surf = skia.Surface(60, 44)
    cv = surf.getCanvas()
    cv.clear(skia.ColorTRANSPARENT)
    glass = skia.Rect.MakeLTRB(10, 4, 50, 40)
    cv.drawRect(glass.makeOutset(4, 4), paint("#060608"))
    cv.drawRect(glass, _radial(30, 22, 26, glow, frame))
    for y in range(6, 40, 6):  # the blinds
        cv.drawRect(skia.Rect.MakeLTRB(10, y, 50, y + 3), paint("#060608", 0.75))
    cv.drawRect(glass.makeOutset(4, 4), paint(frame, stroke=2))
    return png(to_pil(surf))


def dither() -> bytes:
    """The header's mark: a black fedora with a red band, lit along its edge, 48 x 48."""
    surf = skia.Surface(48, 48)
    cv = surf.getCanvas()
    cv.clear(skia.ColorTRANSPARENT)
    hat = union(oval(24, 34, 22, 5.5), svgpath("M12 34L14 16Q19 11 24 15Q29 11 34 16L36 34Z"))
    cv.drawPath(hat, paint("#c8c3b6"))
    cv.save()
    cv.translate(0, 2)
    cv.drawPath(hat, paint("#060608"))
    cv.restore()
    cv.drawRect(skia.Rect.MakeLTRB(13, 27, 35, 31), paint(BLOOD))
    return png(to_pil(surf))


SCENES = {s: png(scene(s)) for s in ("idle", "working", "blocked", "done")}
ICONS = {"dither": dither(), **{f"machine-{name}": machine(*tone) for name, tone in _TONES.items()}}
