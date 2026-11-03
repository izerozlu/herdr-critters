"""Y2K scenes (the sprite box behind each agent, one per machine and per status) and icons.

The look is a desktop wallpaper: a soft sky, a lens flare, clouds and two glossy grass hills.
A scene is 120 x 100; the mod puts the sprite's feet on the front hill's crest (y = 77).
"""

from .kit import orb, spark, svg

SCENE_W, SCENE_H = 120, 100


def scene(sky: list[str], back: str, grass: str, deep: str) -> dict:
    return {"sky": sky, "back": back, "grass": grass, "deep": deep}


def draw_scene(s: dict) -> str:
    top, mid, low = s["sky"]
    defs = (
        f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/>'
        f'<stop offset=".6" stop-color="{mid}"/><stop offset="1" stop-color="{low}"/></linearGradient>'
        f'<linearGradient id="grass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{s["grass"]}"/>'
        f'<stop offset="1" stop-color="{s["deep"]}"/></linearGradient>'
        '<radialGradient id="flare"><stop offset="0" stop-color="#ffffff" stop-opacity=".9"/>'
        '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>'
    )
    cloud = '<g fill="#ffffff" opacity=".85">{}</g>'.format(
        "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}"/>' for x, y, rx, ry in
                ((86, 22, 13, 6), (96, 18, 9, 7), (104, 23, 10, 5), (40, 40, 9, 3.5), (47, 38, 6, 4)))
    )
    body = (
        f'<rect width="{SCENE_W}" height="{SCENE_H}" fill="url(#sky)"/>'
        '<circle cx="16" cy="14" r="16" fill="url(#flare)"/>' + spark(16, 14, 7) + spark(30, 26, 2.5)
        + cloud
        + f'<path d="M0 70Q30 58 70 68T120 64V100H0Z" fill="{s["back"]}"/>'
        + '<path d="M0 82Q60 72 120 82V100H0Z" fill="url(#grass)"/>'
        + '<path d="M10 80.5Q60 72.8 110 80.5" fill="none" stroke="#ffffff" stroke-opacity=".5" stroke-width="1.6" stroke-linecap="round"/>'
    )
    return svg(SCENE_W, SCENE_H, defs, body, scale=2.4)


PALETTES = {
    "bliss": scene(["#2f7fe0", "#5aa2ec", "#a8d4f8"], "#6cc05a", "#4cb83c", "#2a8a2e"),
    "ocean": scene(["#1a9cc8", "#3cbcdc", "#9ae4f2"], "#3aa8c0", "#1f94b8", "#126a8f"),
    "sunset": scene(["#e05a8a", "#f08a7a", "#fbc890"], "#a070d0", "#8a5ac0", "#5f3a90"),
    "grape": scene(["#6a4ac8", "#8a6ae0", "#c4b0f6"], "#e070b8", "#d0509e", "#a83a82"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Mid tones, so every outlined critter still reads.
    "idle": scene(["#8a9ab0", "#a4b2c4", "#d0dae6"], "#a8b6c6", "#8a9aae", "#66768a"),
    "working": scene(["#1e8fe0", "#46b0ee", "#a0dcf8"], "#50c8e0", "#22a8d0", "#1482aa"),
    "blocked": scene(["#d02a5a", "#e2507a", "#f8a0b8"], "#e8789a", "#c03a64", "#8a1e40"),
    "done": scene(["#3aa83a", "#62c44a", "#c0ec90"], "#8ad86a", "#4cb83c", "#1f7024"),
}

# ---- icons


def machine(s: dict) -> str:
    """A round bubble monitor on a foot, in the scene's colors (15 x 11)."""
    top, mid, _ = s["sky"]
    defs = orb("case", "#ffffff", s["grass"]) + orb("screen", mid, top)
    return svg(15, 11, defs, (
        '<rect x="1" y=".6" width="13" height="8" rx="3" fill="url(#case)" stroke="#0b2545" stroke-width=".9"/>'
        '<rect x="3.2" y="2.3" width="8.6" height="4.6" rx="1.4" fill="url(#screen)"/>'
        '<ellipse cx="6" cy="3.4" rx="2.2" ry=".8" fill="#ffffff" opacity=".7"/>'
        f'<path d="M5 10.4H10L9 8.6H6Z" fill="{s["deep"]}"/>'
    ))


ICONS = {
    # The header's mark: a glossy aqua orb.
    "dither": svg(12, 12, orb("ball", "#d8f6ff", "#1e7bff"), (
        '<circle cx="6" cy="6" r="5.2" fill="url(#ball)" stroke="#0b2545" stroke-width=".8"/>'
        '<ellipse cx="5" cy="3.6" rx="2.6" ry="1.4" fill="#ffffff" opacity=".8"/>'
    )),
    **{f"machine-{name}": machine(s) for name, s in PALETTES.items()},
}

SCENES = {name: draw_scene(s) for name, s in PALETTES.items()}
