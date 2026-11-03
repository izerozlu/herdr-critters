"""Cyber scenes (the sprite box behind each agent, one per machine and per status) and icons, as vector SVG."""

from .kit import INK

# 36 x 30 like the retro scenes; the ground (horizon line) is at 23, where the critters stand.
SCENE_W, SCENE_H, HORIZON = 36, 30, 23

# The skyline: (left x, width, height above the horizon).
TOWERS = ((-1, 5, 9), (4, 3.5, 13), (8, 5, 7), (13, 3.5, 15.5), (17, 4.5, 10), (22, 3.5, 12), (25.5, 5, 8), (31, 3.5, 14), (34.5, 3, 6))
# Lit windows, as (x, height above the horizon).
WINDOWS = ((1.2, 6), (2.6, 3), (5.2, 10), (5.2, 7), (9.6, 4), (11.2, 5), (14.4, 12.5), (14.4, 9), (14.4, 4), (18.4, 7), (19.6, 3), (23.4, 9), (26.6, 5), (28.4, 3), (32.4, 11), (32.4, 6))


def scene(sky: list[str], neon: str, floor: str, grid: str, tower: str, window: str) -> str:
    """A night sky, a skyline with lit windows and a neon sign, a glowing horizon and
    a perspective grid floor."""
    w, h, y0 = SCENE_W, SCENE_H, HORIZON
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w * 8}" height="{h * 8}">',
        "<defs>",
        f'<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky[0]}"/>'
        f'<stop offset="0.6" stop-color="{sky[1]}"/><stop offset="1" stop-color="{sky[2]}"/></linearGradient>',
        f'<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{neon}" stop-opacity="0"/>'
        f'<stop offset="1" stop-color="{neon}" stop-opacity="0.35"/></linearGradient>',
        f'<linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{grid}" stop-opacity="0.5"/>'
        f'<stop offset="1" stop-color="{floor}" stop-opacity="1"/></linearGradient>',
        "</defs>",
        f'<rect width="{w}" height="{h}" fill="url(#sky)"/>',
        f'<circle cx="28.5" cy="5" r="2.6" fill="{window}" opacity="0.25"/>',
        f'<circle cx="28.5" cy="5" r="1.6" fill="{window}" opacity="0.6"/>',
        f'<rect y="{y0 - 6}" width="{w}" height="6" fill="url(#haze)"/>',
    ]
    for x, tw, th in TOWERS:
        p.append(f'<rect x="{x}" y="{y0 - th}" width="{tw}" height="{th + 0.5}" rx="0.4" fill="{tower}"/>')
    for x, up in WINDOWS:
        p.append(f'<rect x="{x}" y="{y0 - up}" width="0.9" height="0.7" rx="0.2" fill="{window}" opacity="0.85"/>')
    # A neon sign on the tallest tower, and an antenna light.
    p.append(f'<rect x="12.6" y="{y0 - 8.2}" width="5" height="1.4" rx="0.7" fill="{neon}" opacity="0.35"/>')
    p.append(f'<rect x="13" y="{y0 - 7.9}" width="4.2" height="0.8" rx="0.4" fill="{neon}"/>')
    p.append(f'<path d="M14.75 {y0 - 15.5} V{y0 - 17.5}" stroke="{tower}" stroke-width="0.4"/>')
    p.append(f'<circle cx="14.75" cy="{y0 - 17.6}" r="0.45" fill="{neon}"/>')
    # The floor: a glowing horizon, then grid lines that fan out toward the viewer.
    p.append(f'<rect y="{y0}" width="{w}" height="{h - y0}" fill="url(#floor)"/>')
    for i, gy in enumerate((y0 + 1.4, y0 + 3.2, y0 + 5.6)):
        p.append(f'<path d="M0 {gy} H{w}" stroke="{grid}" stroke-width="{0.3 + i * 0.1}"/>')
    for i in range(-6, 7):
        p.append(f'<path d="M{w / 2 + i * 2.2} {y0} L{w / 2 + i * 7} {h}" stroke="{grid}" stroke-width="0.3"/>')
    p.append(f'<rect y="{y0 - 0.6}" width="{w}" height="1.6" fill="{neon}" opacity="0.3"/>')
    p.append(f'<rect y="{y0 - 0.2}" width="{w}" height="0.6" fill="{neon}"/>')
    p.append("</svg>\n")
    return "".join(p)


def machine(screen: str, glow: str, stand: str) -> str:
    """A monitor on a stand, colored per machine."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 7" width="80" height="56">'
        f'<rect x="0.4" y="0.4" width="9.2" height="4.4" rx="0.9" fill="{screen}" stroke="{glow}" stroke-width="0.8"/>'
        f'<path d="M2 2.2 H5 M2 3.2 H3.6" stroke="{glow}" stroke-width="0.5" stroke-linecap="round"/>'
        f'<path d="M3.6 5.2 L3.2 6.4 H6.8 L6.4 5.2 Z" fill="{stand}"/>'
        "</svg>\n"
    )


# Colors per scene: sky (top, middle, horizon), neon, floor, grid, tower, window.
PALETTES = {
    "neon": (["#0d0618", "#1f0a33", "#3d0f4f"], "#ff4fd8", "#12061c", "#7a2a96", "#08040f", "#ffb3f0"),
    "ice": (["#040c18", "#08182e", "#0c2a44"], "#5ff8ff", "#050e1a", "#1f6a8a", "#02060c", "#a8f8ff"),
    "acid": (["#06120a", "#0b2014", "#123220"], "#7dff6a", "#060f08", "#2a7a36", "#030805", "#c8ffb0"),
    "amber": (["#140a04", "#261206", "#3c1c08"], "#ffb52e", "#120904", "#8a4a12", "#0a0502", "#ffe0a0"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Dark enough that every critter still reads.
    "idle": (["#0b0a12", "#12101c", "#1a1728"], "#7a6f9a", "#0d0c15", "#3a3456", "#07060c", "#4a4466"),
    "working": (["#040c18", "#08182e", "#0c2a44"], "#5ff8ff", "#050e1a", "#1f6a8a", "#02060c", "#a8f8ff"),
    "blocked": (["#14040a", "#260814", "#3a0c1e"], "#ff3b6b", "#12040a", "#7a1838", "#0a0206", "#ffb0c4"),
    "done": (["#06120a", "#0b2014", "#123220"], "#7dff6a", "#060f08", "#2a7a36", "#030805", "#c8ffb0"),
}

SCENES = {name: scene(*pal) for name, pal in PALETTES.items()}

ICONS = {
    # The header mark: two scanlines, magenta over cyan.
    "dither": (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6 6" width="48" height="48">'
        f'<rect x="0.3" y="0.3" width="5.4" height="5.4" rx="1.2" fill="{INK}"/>'
        '<path d="M1.4 2.2 H4.6" stroke="#ff4fd8" stroke-width="0.8" stroke-linecap="round"/>'
        '<path d="M1.4 3.8 H4.6" stroke="#5ff8ff" stroke-width="0.8" stroke-linecap="round"/>'
        "</svg>\n"
    ),
    **{f"machine-{name}": machine(sky[0], neon, grid) for name, (sky, neon, _f, grid, _t, _w) in PALETTES.items()},
}
