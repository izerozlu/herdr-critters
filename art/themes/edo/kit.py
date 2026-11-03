"""Edo drawing kit: woodblock shapes, the face per status, and the status marks.

A sprite is 160 x 128 (the size retro's 20 x 16 grid gives), standing on the
bottom edge. Shapes are flat colors with a thick ink outline, like a print.
The marks sit in the top corners, so a body keeps these clear:
top left x < 34, y < 44 (bolt, "!", check) and top right x > 130, y < 38 (sweat).
"""

INK = "#2a2420"
PAPER = "#f8f4ea"
BLUSH = "#e8908a"
STROKE = 6
FACE = 3.5  # the width of face lines

# Status mark colors, dark enough for the light paper scenes.
GOLD, RED, BLUE, GREEN = "#d08a10", "#c8302a", "#3a6ea8", "#4f7a2e"


def svg(w: int, h: int, body: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>\n'


def _ink(fill: str, stroke: str | None, width: float) -> str:
    line = "" if stroke is None else f' stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"'
    return f'fill="{fill}"{line}'


def path(d: str, fill: str = "none", stroke: str | None = INK, width: float = STROKE) -> str:
    return f'<path d="{d}" {_ink(fill, stroke, width)}/>'


def circle(cx: float, cy: float, r: float, fill: str, stroke: str | None = INK, width: float = STROKE) -> str:
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" {_ink(fill, stroke, width)}/>'


def ellipse(cx: float, cy: float, rx: float, ry: float, fill: str, stroke: str | None = INK, width: float = STROKE) -> str:
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" {_ink(fill, stroke, width)}/>'


def rect(x: float, y: float, w: float, h: float, fill: str, rx: float = 0, stroke: str | None = INK, width: float = STROKE) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" {_ink(fill, stroke, width)}/>'


def face(pose: dict, status: str) -> str:
    """Eyes, mouth and blush for a status. `pose` gives the eyes' centers, the
    mouth's center, the blush spots, the eye size `r` (default 6) and `ink`
    (default INK; a light color for a dark face)."""
    ink, r = pose.get("ink", INK), pose.get("r", 6)
    (mx, my), out = pose["mouth"], []
    for bx, by in pose.get("blush", []):
        out.append(ellipse(bx, by, r * 1.5, r * 0.9, BLUSH, None) if status != "done" else ellipse(bx, by, r * 1.9, r * 1.1, BLUSH, None))
    for i, (x, y) in enumerate(pose["eyes"]):
        if status == "idle":  # shut, a sleepy curve
            out.append(path(f"M{x - r} {y} Q{x} {y + r} {x + r} {y}", stroke=ink, width=FACE))
        elif status == "done":  # happy, an upturned arc
            out.append(path(f"M{x - r} {y + 1} Q{x} {y - r - 1} {x + r} {y + 1}", stroke=ink, width=FACE))
        elif status == "blocked":  # red eyes under worried brows
            out.append(circle(x, y, r, RED, None))
            tilt = -1 if i == 0 else 1
            out.append(path(f"M{x - r} {y - r - 3 + tilt * 2} L{x + r} {y - r - 3 - tilt * 2}", stroke=ink, width=FACE))
        else:  # open, with a glint
            out.append(circle(x, y, r, ink, None))
            out.append(circle(x + r * 0.35, y - r * 0.35, r * 0.35, PAPER, None))
    mouth = {
        "idle": path(f"M{mx - 4} {my} L{mx + 4} {my}", stroke=ink, width=FACE),
        "working": path(f"M{mx - 6} {my} Q{mx} {my + 5} {mx + 6} {my}", stroke=ink, width=FACE),
        "blocked": ellipse(mx, my + 1, 4, 5, ink, None),
        "done": path(f"M{mx - 8} {my - 1} Q{mx} {my + 11} {mx + 8} {my - 1} Z", fill=RED, stroke=ink, width=FACE),
    }[status]
    return "".join(out) + mouth


def marks(status: str) -> str:
    """The status mark in the top corners: a bolt, a "!" and a sweat drop, or a check."""
    if status == "working":
        return path("M22 4 L10 22 L18 22 L12 38 L28 16 L20 16 Z", GOLD, INK, 2.5)
    if status == "blocked":
        return rect(11, 4, 9, 24, RED, 3, INK, 2.5) + circle(15.5, 36, 5, RED, INK, 2.5) + path(
            "M142 8 Q134 22 136 28 Q142 36 148 28 Q150 22 142 8 Z", BLUE, INK, 2.5
        )
    if status == "done":
        return path("M6 22 L16 32 L32 10", stroke=INK, width=9) + path("M6 22 L16 32 L32 10", stroke=GREEN, width=5)
    return ""


def sprite(body: str, pose: dict, status: str) -> str:
    """A whole sprite: the body, the extra shapes for this status, the face, then the mark."""
    return svg(160, 128, body + pose.get(status, "") + face(pose, status) + marks(status))
