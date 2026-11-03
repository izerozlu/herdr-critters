"""Shared drawing kit for the cyber critters: flat vector mascots with holo chrome.

Every critter is drawn in a 40 x 32 box, standing on the bottom edge, with a dark
INK outline, one cel shadow per part (SHADE), holo gradients on chrome and neon
details that light up when the agent works. No SVG filters: glows are radial
gradients that fade out.

A critter is a function `draw(status) -> str` that returns the SVG body. Use the
helpers here for eyes, mouths and status marks, so all critters act alike.
"""

W, H = 40, 32

INK = "#140a26"  # outline
SW = 1.2  # main outline width
SHADE = "#7a5cd6"  # cel shadow tint, drawn at SHADE_OP
SHADE_OP = "0.45"

# Neon colors by key, lit and dim (the dim one is the light when it is off).
NEON = {
    "m": ("#ff4fd8", "#6a3a6e"),  # magenta
    "c": ("#5ff8ff", "#2f6a7a"),  # cyan
    "a": ("#ffb52e", "#6a4a24"),  # amber
    "g": ("#7dff6a", "#2f5a34"),  # acid green
    "v": ("#a87bff", "#3f3466"),  # violet
    "r": ("#ff3b6b", "#6a2434"),  # red
}
BLOCKED = "r"  # eye and mark color of a blocked critter
DONE = "g"
BOLT = "#fcee0a"


def lit(key: str, on: bool = True) -> str:
    return NEON[key][0 if on else 1]


DEFS = (
    "<defs>"
    # Pale holo chrome for bodies, a saturated one for trims and inner ears.
    '<linearGradient id="holo" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#ffd0f4"/><stop offset="0.35" stop-color="#e6dcff"/>'
    '<stop offset="0.6" stop-color="#c2b2ff"/><stop offset="1" stop-color="#86ecff"/></linearGradient>'
    '<linearGradient id="holoDark" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#ff5fd2"/><stop offset="1" stop-color="#3fd8ff"/></linearGradient>'
    # Gunmetal for dark armor.
    '<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#8a90b8"/><stop offset="1" stop-color="#3a3f62"/></linearGradient>'
    # A dark screen or visor glass.
    '<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#0d1d3a"/><stop offset="1" stop-color="#071022"/></linearGradient>'
    + "".join(
        f'<radialGradient id="glow-{k}" cx="0.5" cy="0.5" r="0.5">'
        f'<stop offset="0" stop-color="{on}" stop-opacity="0.75"/>'
        f'<stop offset="1" stop-color="{on}" stop-opacity="0"/></radialGradient>'
        for k, (on, _off) in NEON.items()
    )
    + "</defs>"
)


def sprite(draw, status: str) -> str:
    """The whole sprite SVG for a critter's draw function and a status. The size is the
    retro grid's (20 x 16) times 8, like the other themes, so previews line up."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="160" height="128">'
        f"{DEFS}{draw(status)}</svg>\n"
    )


def glow(cx: float, cy: float, rx: float, key: str, ry: float | None = None, opacity: float = 1) -> str:
    """A soft light behind a neon part. Draw it before the part."""
    return (
        f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry if ry is not None else rx}" '
        f'fill="url(#glow-{key})" opacity="{opacity}"/>'
    )


def shape(d: str, fill: str = "url(#holo)", width: float = SW) -> str:
    """A part: a filled path with the ink outline."""
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def shade(d: str) -> str:
    """A cel shadow shape, no outline. Put it on the side away from the top-left light."""
    return f'<path d="{d}" fill="{SHADE}" opacity="{SHADE_OP}"/>'


def line(d: str, color: str, width: float = 0.6, opacity: float = 1) -> str:
    return (
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
        f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>'
    )


def cable(d: str, color: str, width: float = 1.6) -> str:
    """A thick tube: an ink stroke with a colored stroke on top."""
    return line(d, INK, width + 1.6) + line(d, color, width)


def highlight(d: str) -> str:
    """The white shine on a top-left edge."""
    return line(d, "#ffffff", 0.8, 0.9)


def eyes(status: str, centers: list[tuple[float, float]], key: str = "c", r: float = 1.2) -> str:
    """Standard eyes: idle closed arcs, working lit pills with a glint, blocked red
    pills under angry brows, done happy upturned arcs."""
    out = []
    for cx, cy in centers:
        if status == "idle":
            out.append(line(f"M{cx - r} {cy - 0.2} Q{cx} {cy + r} {cx + r} {cy - 0.2}", lit(key, False), 0.7))
        elif status == "done":
            out.append(line(f"M{cx - r} {cy + 0.5} Q{cx} {cy - r} {cx + r} {cy + 0.5}", lit(DONE), 0.75))
        else:
            k = BLOCKED if status == "blocked" else key
            out.append(glow(cx, cy, r * 2.2, k, opacity=0.8))
            out.append(f'<rect x="{cx - r}" y="{cy - r * 1.2}" width="{2 * r}" height="{2.4 * r}" rx="{r}" fill="{lit(k)}"/>')
            out.append(f'<circle cx="{cx - r * 0.35}" cy="{cy - r * 0.55}" r="{r * 0.35}" fill="#ffffff"/>')
    if status == "blocked" and len(centers) >= 2:
        (lx, ly), (rx, ry) = centers[0], centers[-1]
        out.append(line(f"M{lx - r * 1.2} {ly - r * 2.1} L{lx + r} {ly - r * 1.5}", INK, 0.7))
        out.append(line(f"M{rx + r * 1.2} {ry - r * 2.1} L{rx - r} {ry - r * 1.5}", INK, 0.7))
    return "".join(out)


def mouth(status: str, cx: float, cy: float, w: float = 1.8, color: str = INK) -> str:
    """Standard mouth: idle flat, working small smile, blocked wobbly frown, done open grin."""
    h = w / 2
    if status == "idle":
        return line(f"M{cx - h * 0.6} {cy} H{cx + h * 0.6}", color, 0.55)
    if status == "working":
        return line(f"M{cx - h} {cy - 0.2} Q{cx} {cy + 0.9} {cx + h} {cy - 0.2}", color, 0.6)
    if status == "blocked":
        return line(f"M{cx - h} {cy + 0.5} Q{cx - h / 2} {cy - 0.4} {cx} {cy + 0.1} Q{cx + h / 2} {cy - 0.4} {cx + h} {cy + 0.5}", color, 0.6)
    return f'<path d="M{cx - h} {cy - 0.3} Q{cx} {cy + 1.8} {cx + h} {cy - 0.3} Z" fill="{lit("m")}" stroke="{color}" stroke-width="0.5" stroke-linejoin="round"/>'


def mark(status: str, x: float, y: float) -> str:
    """The status mark in free space, its top left at (x, y), about 3 x 5 units:
    working a bolt, blocked a "!" and a sweat drop, done a check. Idle has none."""
    if status == "working":
        d = f"M{x + 2} {y} L{x} {y + 2.8} H{x + 1.5} L{x + 0.8} {y + 5} L{x + 3} {y + 2} H{x + 1.5} Z"
        return glow(x + 1.5, y + 2.5, 3, "a", opacity=0.6) + shape(d, BOLT, 0.6)
    if status == "blocked":
        red = lit(BLOCKED)
        return (
            glow(x + 0.9, y + 2.5, 2.6, BLOCKED, opacity=0.6)
            + f'<rect x="{x + 0.2}" y="{y}" width="1.4" height="3.3" rx="0.7" fill="{red}" stroke="{INK}" stroke-width="0.5"/>'
            + f'<circle cx="{x + 0.9}" cy="{y + 4.4}" r="0.75" fill="{red}" stroke="{INK}" stroke-width="0.5"/>'
            + f'<path d="M{x + 3.2} {y + 0.6} Q{x + 4.2} {y + 2} {x + 3.2} {y + 2.6} Q{x + 2.2} {y + 2} {x + 3.2} {y + 0.6} Z" '
            f'fill="{lit("c")}" stroke="{INK}" stroke-width="0.4"/>'
        )
    if status == "done":
        d = f"M{x} {y + 2.6} L{x + 1.2} {y + 3.8} L{x + 3.2} {y + 0.8}"
        return glow(x + 1.6, y + 2.4, 2.8, DONE, opacity=0.6) + line(d, INK, 1.7) + line(d, lit(DONE), 0.8)
    return ""
