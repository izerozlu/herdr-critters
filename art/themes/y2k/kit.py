"""The y2k drawing kit: glossy vector critters with one face engine for every status.

A sprite is 100 x 80 (the 5:4 box the mod draws it in); the feet touch y = 80.
A critter gives its body and where its face sits; the kit draws the eyes, the
mouth, the blush and the status marks, so every critter poses the same way.
Keep the top corners (x < 22 or x > 78, y < 34) free: the marks go there.
"""

from dataclasses import dataclass, field

W, H = 100, 80
INK = "#0b2545"  # the outline of every shape


def line(width: float = 3) -> str:
    """Outline attributes: ink color, round joins, `width` thick."""
    return f'stroke="{INK}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"'


LINE = line()
STATUSES = ("idle", "working", "blocked", "done")

# Mark colors, matched to theme.js status colors.
GLOW, BAD, SWEAT, GOOD, BLUSH = "#ffd23a", "#ff2a6d", "#3aa0ff", "#2fc84a", "#ff8ac2"


def gloss(gid: str, light: str, mid: str, dark: str) -> str:
    """A top-to-bottom plastic gradient: light top, base middle, dark bottom."""
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{light}"/><stop offset=".55" stop-color="{mid}"/>'
        f'<stop offset="1" stop-color="{dark}"/></linearGradient>'
    )


def orb(gid: str, light: str, dark: str) -> str:
    """A round gradient lit from the top left, for balls and bubbles."""
    return (
        f'<radialGradient id="{gid}" cx=".35" cy=".3" r=".8">'
        f'<stop offset="0" stop-color="{light}"/><stop offset="1" stop-color="{dark}"/></radialGradient>'
    )


def shine(cx: float, cy: float, rx: float, ry: float) -> str:
    """The Aqua gloss: a white highlight that fades to clear at its bottom."""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="url(#shine)"/>'


def spark(cx: float, cy: float, r: float, color: str = "#ffffff") -> str:
    """A four-point twinkle."""
    q = r * 0.28
    return (
        f'<path d="M{cx} {cy - r}L{cx + q} {cy - q}L{cx + r} {cy}L{cx + q} {cy + q}'
        f'L{cx} {cy + r}L{cx - q} {cy + q}L{cx - r} {cy}L{cx - q} {cy - q}Z" fill="{color}"/>'
    )


SHARED_DEFS = (
    '<linearGradient id="shine" x1="0" y1="0" x2="0" y2="1">'
    '<stop offset="0" stop-color="#ffffff" stop-opacity=".95"/>'
    '<stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>'
    + orb("badge-bad", "#ff9ab8", BAD)
    + orb("badge-good", "#b8ffb0", GOOD)
    + orb("drop", "#d8f0ff", SWEAT)
    + orb("bolt", "#fff6c0", GLOW)
)


@dataclass
class Critter:
    defs: str  # gradients the body uses; prefix ids with the critter name
    body: str  # the shapes, drawn first, outlined with LINE
    eyes: list[tuple[float, float]]  # eye centers
    mouth: tuple[float, float]  # mouth center
    eye: float = 3.5  # eye radius; 3 to 4.5 reads at the small size
    lit: str = ""  # shapes drawn on top only while working: lights, screens, glow
    extra: dict[str, str] = field(default_factory=dict)  # more shapes per status, on top of the face


def face(c: Critter, status: str) -> str:
    r, (mx, my) = c.eye, c.mouth
    out: list[str] = []
    for x, y in c.eyes:
        if status == "idle":  # closed, sleepy
            out.append(f'<path d="M{x - r} {y}Q{x} {y + r * 0.9} {x + r} {y}" fill="none" {line(2.4)}/>')
        elif status == "blocked":  # squeezed shut: > <
            s = -1 if x < mx else 1
            out.append(
                f'<path d="M{x - s * r} {y - r}L{x + s * r * 0.6} {y}L{x - s * r} {y + r}" fill="none" '
                f'stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>'
            )
        elif status == "done":  # happy arcs: ^ ^
            out.append(f'<path d="M{x - r} {y + r * 0.5}Q{x} {y - r * 1.3} {x + r} {y + r * 0.5}" fill="none" {line(2.6)}/>')
        else:  # open, with a catchlight
            out.append(f'<ellipse cx="{x}" cy="{y}" rx="{r * 0.85}" ry="{r * 1.15}" fill="{INK}"/>')
            out.append(f'<circle cx="{x - r * 0.3}" cy="{y - r * 0.45}" r="{r * 0.38}" fill="#ffffff"/>')
    if status == "idle":
        out.append(f'<path d="M{mx - 3} {my}L{mx + 3} {my}" {line(2.2)}/>')
    elif status == "working":
        out.append(f'<path d="M{mx - 4} {my - 1}Q{mx} {my + 3} {mx + 4} {my - 1}" fill="none" {line(2.2)}/>')
    elif status == "blocked":  # a wobbly worried mouth
        out.append(f'<path d="M{mx - 5} {my + 1}Q{mx - 2.5} {my - 2} {mx} {my + 1}Q{mx + 2.5} {my + 4} {mx + 5} {my + 1}" fill="none" {line(2.2)}/>')
    else:  # a wide open smile and blush
        out.append(f'<path d="M{mx - 5.5} {my - 1.5}Q{mx} {my + 7} {mx + 5.5} {my - 1.5}Z" fill="#ff5a8a" {line(2)}/>')
        for x, y in c.eyes[:1] + c.eyes[-1:]:
            dx = -r * 0.9 if x < mx else r * 0.9
            out.append(f'<ellipse cx="{x + dx}" cy="{y + r * 2}" rx="{r * 0.9}" ry="{r * 0.5}" fill="{BLUSH}" opacity=".85"/>')
    return "".join(out)


def marks(status: str) -> str:
    """Status marks in the top corners: a bolt, a ! badge and a sweat drop, a check badge."""
    if status == "working":
        return (
            f'<path d="M14 4L5 19H11L8 31L19 14H13L16 4Z" fill="url(#bolt)" {line(2)}/>'
            + spark(88, 8, 5, GLOW)
        )
    if status == "blocked":
        return (
            f'<circle cx="11" cy="13" r="9" fill="url(#badge-bad)" {line(2)}/>'
            f'<path d="M11 7.5V14" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round"/>'
            '<circle cx="11" cy="18.2" r="1.7" fill="#ffffff"/>'
            f'<path d="M88 6Q83 14 83 17A5 5 0 0 0 93 17Q93 14 88 6Z" fill="url(#drop)" {line(2)}/>'
        )
    if status == "done":
        return (
            f'<circle cx="11" cy="13" r="9" fill="url(#badge-good)" {line(2)}/>'
            '<path d="M6.5 13.5L10 17L16 9.5" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
            + spark(88, 9, 5)
        )
    return ""


def svg(w: int, h: int, defs: str, body: str, scale: float = 2) -> str:
    """An SVG document. Its width and height are the viewBox times `scale`; sprites and
    scenes use the pixel themes' sizes (grid times 8) so art/preview.py lines them up."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{round(w * scale)}" height="{round(h * scale)}">'
        f"<defs>{defs}</defs>{body}</svg>\n"
    )


def sprite(c: Critter, status: str) -> str:
    """One critter's SVG for one status."""
    return svg(
        W, H, SHARED_DEFS + c.defs,
        c.body + (c.lit if status == "working" else "") + face(c, status) + c.extra.get(status, "") + marks(status),
        scale=1.6,
    )
