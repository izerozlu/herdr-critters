"""Deepsea scenes (the sprite box behind each agent, one per machine and per status) and icons.

The look is soft deep water: light shafts from the surface, out of focus glow and a dim
seabed, all in one accent color. A scene is 120 x 100, saved as 576 x 480; the mod puts
the sprite's feet on the seabed's crest (y = 80).
"""

from .kit import BG, DIVE, DOCK, DRIFT, SOS, WHITE, canvas, fill, gel, glow, linear, mix, png
from .paths import circle, path

SCENE_W, SCENE_H = 120, 100
DEEP = "#04060e"  # the bottom of every scene


def draw_scene(accent: str, base: str = BG) -> bytes:
    surface, c = canvas(SCENE_W, SCENE_H, 4.8)
    c.drawRect(c.getLocalClipBounds(), linear(0, 0, 0, 100, [
        (0, mix(base, accent, 0.28), 1), (0.55, mix(base, accent, 0.08), 1), (1, DEEP, 1)]))
    for x0, w in ((22, 14), (52, 20), (90, 12)):  # light shafts from the surface
        shaft = path(f"M{x0} -6L{x0 + w} -6L{x0 + w * 0.6 + 22} 80L{x0 + 4} 80Z")
        c.drawPath(shaft, linear(0, 0, 0, 80, [(0, accent, 0.16), (1, accent, 0)], blur=5))
    for x, y, r, a in ((12, 22, 5, 0.22), (104, 16, 7, 0.18), (96, 58, 4, 0.25), (18, 60, 3, 0.3), (70, 8, 3, 0.2),
                       (40, 40, 2, 0.2), (110, 40, 2.5, 0.3)):  # out of focus glow
        c.drawCircle(x, y, r, fill(mix(accent, WHITE, 0.3), a, blur=r * 0.7))
    floor = path("M0 84Q30 77 60 80T120 82V100H0Z")
    c.drawPath(floor, fill(accent, 0.25, blur=3))
    c.drawPath(floor, linear(0, 78, 0, 100, [(0, mix(base, accent, 0.3), 1), (1, DEEP, 1)]))
    for x, y in ((8, 81), (16, 82), (100, 80), (110, 81), (60, 86)):  # glowing grains on the seabed
        c.drawCircle(x, y, 0.8, fill(mix(accent, WHITE, 0.5), 0.8, blur=0.6))
    return png(surface)


# Status scenes take the status color; machine scenes take theme.js scenes' label over their card.
PALETTES = {
    "abyss": ("#7ffcff", "#0c1430"),
    "reef": ("#ffb8f4", "#1a1030"),
    "vent": ("#ffc08a", "#1e1018"),
    "trench": ("#9fffd8", "#0a1c20"),
    "idle": (DRIFT, BG),
    "working": (DIVE, BG),
    "blocked": (SOS, BG),
    "done": (DOCK, BG),
}

SCENES = {name: draw_scene(*pal) for name, pal in PALETTES.items()}


# ---- icons


def machine(accent: str) -> bytes:
    """A small gel submarine in the scene's color (15 x 11, saved at 4x)."""
    surface, c = canvas(15, 11, 4)
    gel(c, path("M3 4.6H11.4Q14 4.6 14 7.3Q14 10 11.4 10H3.6Q1 10 1 7.3Q1 4.6 3 4.6Z"), accent)
    gel(c, path("M5 4.8V2.6Q5 1.6 6 1.6H8Q9 1.6 9 2.6V4.8Z"), accent)
    c.drawCircle(6, 7.3, 1.3, fill(DEEP, 0.85))
    c.drawCircle(10, 7.3, 1.3, fill(DEEP, 0.85))
    glow(c, 6, 7.3, 0.6, WHITE)
    glow(c, 10, 7.3, 0.6, WHITE)
    return png(surface)


def dither() -> bytes:
    """The header's mark: a glowing gel orb (12 x 12, saved at 4x)."""
    surface, c = canvas(12, 12, 4)
    gel(c, circle(6, 6, 4.6), DIVE)
    glow(c, 6, 6.4, 1.2, WHITE, 0.8)
    return png(surface)


ICONS = {
    "dither": dither(),
    **{f"machine-{name}": machine(accent) for name, (accent, _) in PALETTES.items()},
}
