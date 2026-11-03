"""Garden scenes (the sprite box behind each agent, one per machine and per status) and icons.

A scene is a felt picture of 288 x 240 units: a felt backdrop, a stitched sun and cloud,
two layered felt hills and felt flowers at the sides. The mod puts the sprite's feet on
the front hill, about 7/30 up from the bottom (y ~ 186).
"""

import math

import numpy as np

from .kit import SS, Canvas, felt, inset, mask, noise, outline_of, qbez, rgb, stitch, thread_of

W, H = 288, 240


def scene(bg: str, hill: str, ground: str) -> dict:
    return {"bg": bg, "hill": hill, "ground": ground}


def draw_scene(s: dict) -> bytes:
    cv = Canvas(W, H)
    fib = noise(cv.shape, 0.5 * SS, 1, octaves=2)
    mott = noise(cv.shape, 8 * SS, 2, octaves=2)
    cv.c[:] = rgb(s["bg"]) * (0.93 + 0.08 * fib[..., None] + 0.04 * mott[..., None])
    cv.a[:] = 1
    sun = ("circle", 258, 38, 17)
    felt(cv, mask(W, H, [sun]), "#f6c64a", 5, puff=5, drop=2)
    stitch(cv, inset(outline_of(sun), 3), thread_of("#f6c64a"))
    cloud = [("ellipse", 150, 26, 20, 9), ("ellipse", 162, 19, 12, 10), ("ellipse", 142, 21, 9, 7)]
    felt(cv, mask(W, H, cloud), "#fbf7ee", 6, puff=4, drop=1.6)
    for top, color, seed in (
        (qbez((0, 156), (80, 124), (160, 160)) + qbez((160, 160), (230, 138), (288, 148)), s["hill"], 7),
        (qbez((-2, 190), (144, 178), (290, 192)), s["ground"], 8),
    ):
        felt(cv, mask(W, H, [("poly", [(0, 240)] + top + [(288, 240)])]), color, seed, puff=7, drop=2.3)
        stitch(cv, [(x, y + 4) for x, y in top], thread_of(color))
    for x, y, petal in ((24, 170, "#ef8fb0"), (266, 166, "#f5c445"), (276, 184, "#ef8fb0"), (12, 186, "#f5c445")):
        felt(cv, mask(W, H, [("line", [(x, y), (x + 1, y + 30)], 2.2)]), "#5f8a46", x, puff=1, drop=0.8)
        petals = [("circle", x + 5 * math.cos(a), y + 5 * math.sin(a), 4.2) for a in np.linspace(0, 2 * math.pi, 5, endpoint=False)]
        felt(cv, mask(W, H, petals), petal, x + 1, puff=3, drop=1.2)
        felt(cv, mask(W, H, [("circle", x, y, 2.6)]), "#a0642e" if petal == "#f5c445" else "#f5c445", x + 2, puff=1.5, drop=0.5)
    return cv.png(2)


PALETTES = {
    # One per machine, in the theme.js scene colors (card, edge, box).
    "greenhouse": scene("#e9f0dc", "#c9dbb2", "#a9c88e"),
    "barrow": scene("#f6ead8", "#e5cfb0", "#d4b088"),
    "seeds": scene("#efe8f3", "#d9cbe6", "#bca6d6"),
    "pond": scene("#e4eff3", "#c4dce6", "#9cc4d8"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Light felt, so every critter reads.
    "idle": scene("#e6dfca", "#c6c3a6", "#a5a886"),
    "working": scene("#f7e3a4", "#bcd69c", "#8ec272"),
    "blocked": scene("#f4c3b8", "#dfc79e", "#bba97a"),
    "done": scene("#d4ecbe", "#a8d790", "#76b864"),
}

# ---- icons

# The pot and flower colors each machine icon takes: (pot, flower).
_TONES = {
    "greenhouse": ("#4f8a3c", "#f5c445"), "barrow": ("#a0522d", "#ef8fb0"), "seeds": ("#7a5aa8", "#f5c445"), "pond": ("#2f7aa8", "#fbf3e2"),
    "idle": ("#8c8471", "#e6dfca"), "working": ("#b87400", "#f5c445"), "blocked": ("#cc3b3b", "#f4c3b8"), "done": ("#3d8b37", "#f5c445"),
}


def flowerpot(pot: str, flower: str) -> bytes:
    """A machine: a felt flower pot, 30 x 22, in the scene's colors."""
    cv = Canvas(30, 22)
    felt(cv, mask(30, 22, [("line", [(15, 13), (15, 6)], 1.4)]), "#5f8a46", 1, puff=0.6, drop=0.3, fuzz=0.3)
    felt(cv, mask(30, 22, [("ellipse", 11, 9, 3.2, 1.6), ("ellipse", 19, 8, 3.2, 1.6)]), "#6fae4a", 2, puff=0.8, drop=0.3, fuzz=0.3)
    felt(cv, mask(30, 22, [("circle", 15, 4.5, 3.6)]), flower, 3, puff=1, drop=0.4, fuzz=0.3)
    felt(cv, mask(30, 22, [("poly", [(8, 13), (22, 13), (20, 21), (10, 21)])]), pot, 4, puff=1.4, drop=0.5, fuzz=0.3)
    felt(cv, mask(30, 22, [("rect", 6.5, 11.5, 23.5, 15)]), pot, 5, puff=1, drop=0.5, fuzz=0.3)
    return cv.png(2)


def daisy() -> bytes:
    """The header's mark: a felt flower, 12 x 12."""
    cv = Canvas(12, 12)
    petals = [("circle", 6 + 3 * math.cos(a), 6 + 3 * math.sin(a), 2.4) for a in np.linspace(0, 2 * math.pi, 5, endpoint=False)]
    felt(cv, mask(12, 12, petals), "#ef8fb0", 1, puff=1, drop=0.3, fuzz=0.2)
    felt(cv, mask(12, 12, [("circle", 6, 6, 1.8)]), "#f5c445", 2, puff=0.6, drop=0.2, fuzz=0.2)
    return cv.png(3)


SCENES = {name: draw_scene(s) for name, s in PALETTES.items()}
ICONS = {"dither": daisy(), **{f"machine-{name}": flowerpot(*tone) for name, tone in _TONES.items()}}
