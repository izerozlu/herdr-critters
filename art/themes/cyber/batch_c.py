"""Critters batch C: spike, binary, zero, omega, ghost, hydra, karma, nitro, pulse, wire."""

import math

from .kit import INK, SW, cable, eyes, glow, highlight, line, lit, mark, mouth, shade, shape


def grad(gid: str, c0: str, c1: str) -> str:
    """A diagonal two-stop body gradient, for a critter's own inline defs."""
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/></linearGradient>'
    )


def socket(cx: float, cy: float, rx: float, ry: float) -> str:
    """A dark eye socket, so the kit eyes read on a light face."""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{INK}"/>'


def spike(s: str) -> str:
    """A punk hedgehog with a neon mohawk of spikes and a studded collar."""
    on = s == "working"
    p = ["<defs>" + grad("spike-quill", "#a8605a", "#4a2440") + grad("spike-face", "#ffe6c8", "#e8a272")]
    p.append('<linearGradient id="spike-hawk" x1="0" y1="1" x2="0" y2="0">')
    p.append(f'<stop offset="0" stop-color="{lit("m")}"/><stop offset="1" stop-color="{lit("c")}"/></linearGradient></defs>')
    # The quills: a zigzag dome around the face.
    pts = []
    for i in range(23):
        t = math.radians(-28 + i * 236 / 22)
        rx, ry = (15, 12.6) if i % 2 == 0 else (12, 9.8)
        pts.append(f"{20 + rx * math.cos(t):.1f} {21.5 - ry * math.sin(t):.1f}")
    p.append(shape("M" + " L".join(pts) + " L11 31.2 H29 Z", "url(#spike-quill)"))
    p.append(shade("M31 13.5 L35 17 L32.5 20 L35.8 24.5 L32 27.5 L29 30.5 L27 29 C29.5 24 30.5 18.5 31 13.5 Z"))
    p.append(highlight("M7.6 17.6 L10 15.4 M10.6 12.6 L13.2 11.2"))
    # The mohawk: lit neon when working, a red alarm when blocked.
    if on:
        p.append(glow(20, 5, 9, "m", ry=6))
    hawk = "url(#spike-hawk)" if on else lit("r") if s == "blocked" else lit("m", False)
    p.append(shape("M13 11.5 L12.6 5 L15.6 9.2 L16.3 2.2 L18.6 8.6 L20 1.2 L21.4 8.6 L23.7 2.2 L24.4 9.2 L27.4 5 L27 11.5 Z", hawk))
    p.append(shape("M20 12.6 C26.6 12.6 29.6 17 29.6 22.2 C29.6 27.6 25.6 31.2 20 31.2 C14.4 31.2 10.4 27.6 10.4 22.2 C10.4 17 13.4 12.6 20 12.6 Z", "url(#spike-face)"))
    p.append(shade("M27.2 15.6 C29 17.6 29.6 20 29.6 22.2 C29.6 27.6 25.6 30.6 21 30.9 C25.6 28.4 28.2 22.6 27.2 15.6 Z"))
    p.append(highlight("M13 16.2 C14.2 14.6 15.8 13.8 17.6 13.5"))
    # A punk domino mask with the eyes in it.
    p.append(f'<path d="M11.4 18.6 C15 17.8 18 18.4 20 19.4 C22 18.4 25 17.8 28.6 18.6 L28 21.6 C25 22.8 22 22.4 20 21.6 C18 22.4 15 22.8 12 21.6 Z" fill="{INK}"/>')
    p.append(eyes(s, [(16, 20.2), (24, 20.2)], "m", 1.1))
    p.append(f'<ellipse cx="20" cy="23.6" rx="1.4" ry="1" fill="{INK}"/>')
    p.append('<circle cx="19.5" cy="23.3" r="0.35" fill="#ffffff"/>')
    p.append(mouth(s, 20, 25.6, 2.4))
    # The studded collar.
    p.append(f'<path d="M11.6 27 C16 28.8 24 28.8 28.4 27 L28.8 29.2 C24 31 16 31 11.2 29.2 Z" fill="{INK}"/>')
    p.append(line("M12.2 28.4 C16 29.8 24 29.8 27.8 28.4", lit("m", on), 0.45))
    for x in (13.6, 17, 20, 23, 26.4):
        p.append(f'<circle cx="{x}" cy="{28.6 + 0.6 * (1 - abs(x - 20) / 6.4)}" r="0.55" fill="#e8ecff"/>')
    for cx in (15, 25):
        p.append(f'<ellipse cx="{cx}" cy="30.9" rx="2.6" ry="1" fill="url(#spike-quill)" stroke="{INK}" stroke-width="1"/>')
    p.append(mark(s, 2, 2))
    return "".join(p)


def binary(s: str) -> str:
    """A small boxy robot whose eyes turn into a 1 and a 0, with bits on its chest panel."""
    on = s == "working"
    p = ["<defs>" + grad("binary-shell", "#9cccff", "#3456c8") + "</defs>"]

    def bit(ch: str, x: float, y: float, h: float, color: str) -> str:
        """A 1 or a 0 glyph, its center at (x, y), h tall."""
        if ch == "1":
            return line(f"M{x - h * 0.2} {y - h * 0.3} L{x} {y - h / 2} V{y + h / 2}", color, h * 0.2)
        return f'<ellipse cx="{x}" cy="{y}" rx="{h * 0.25}" ry="{h * 0.4}" fill="none" stroke="{color}" stroke-width="{h * 0.17}"/>'

    for side in (1, -1):
        hx = 20 + side * 12.4
        p.append(cable(f"M{20 + side * 8.5} 20.5 C{20 + side * 11.5} 20.5 {hx} 21.5 {hx} 24.5", "#4f6fd8", 1.4))
        p.append(f'<path d="M{hx - 1.6} 24.6 H{hx + 1.6} L{hx + 1} 27.2 M{hx - 1.6} 24.6 L{hx - 1} 27.2" fill="#c8d0ff" stroke="{INK}" stroke-width="0.9" stroke-linejoin="round" stroke-linecap="round"/>')
    for x in (13.6, 22.4):
        p.append(f'<rect x="{x}" y="27" width="4" height="3" fill="#2a3a7a" stroke="{INK}" stroke-width="1"/>')
        p.append(f'<rect x="{x - 1}" y="29.4" width="6" height="1.8" rx="0.9" fill="url(#binary-shell)" stroke="{INK}" stroke-width="1"/>')
    # The body, with a bit panel on the chest.
    p.append(f'<rect x="11" y="17.4" width="18" height="10.6" rx="2.6" fill="url(#binary-shell)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M25.6 18 H26.6 C27.8 18 28.4 18.8 28.4 20 V25.6 C28.4 26.8 27.6 27.4 26.4 27.4 H24.6 C25.8 25 26 21 25.6 18 Z"))
    p.append(f'<rect x="14" y="19.6" width="10.6" height="6" rx="1.2" fill="{INK}"/>')
    p.append('<rect x="14.7" y="20.3" width="9.2" height="4.6" rx="0.8" fill="url(#screen)"/>')
    key = "r" if s == "blocked" else "g"
    if on or s == "blocked":
        p.append(glow(19.3, 22.6, 6, key, ry=3.5, opacity=0.7))
    for i, ch in enumerate("1011" if s != "blocked" else "0000"):
        p.append(bit(ch, 16.2 + i * 2.1, 22.6, 2.8, lit(key, on or s == "blocked")))
    p.append(f'<circle cx="26.6" cy="22.6" r="0.7" fill="{lit("m", on)}"/>')
    p.append(f'<rect x="17.6" y="16.4" width="4.8" height="1.6" fill="#2a3a7a" stroke="{INK}" stroke-width="0.9"/>')
    # The head: ear bolts, the antenna and the face screen.
    for side in (1, -1):
        p.append(f'<rect x="{20 + side * 12.4 - 1.2}" y="9" width="2.4" height="5.4" rx="0.8" fill="#c8d0ff" stroke="{INK}" stroke-width="1"/>')
    p.append(line("M20 5.6 V2.8", INK, 0.9))
    if on:
        p.append(glow(20, 2.2, 2.2, "g"))
    p.append(f'<circle cx="20" cy="2.2" r="1" fill="{lit("g", on)}" stroke="{INK}" stroke-width="0.6"/>')
    p.append(f'<rect x="8.4" y="5.6" width="23.2" height="12" rx="3.2" fill="url(#binary-shell)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M28.4 6.2 C30.2 6.6 31 7.6 31 9.4 V14.4 C31 16.2 29.8 17 28.2 17 H26 C28.4 14 29 9.6 28.4 6.2 Z"))
    p.append(highlight("M10.2 9.6 C10.2 7.8 11 7 12.6 6.8"))
    p.append(f'<rect x="11" y="7.8" width="18" height="8" rx="2" fill="{INK}"/>')
    p.append('<rect x="11.8" y="8.6" width="16.4" height="6.4" rx="1.5" fill="url(#screen)"/>')
    if on:
        for x, ch in ((16, "1"), (24, "0")):
            p.append(glow(x, 11.2, 2.8, "g", opacity=0.8))
            p.append(bit(ch, x, 11.2, 3.6, lit("g")))
    else:
        p.append(eyes(s, [(16, 11.2), (24, 11.2)], "g", 1.1))
    p.append(mouth(s, 20, 13.8, 2.2, lit("g")))
    p.append(mark(s, 2.5, 2.5))
    return "".join(p)


def zero(s: str) -> str:
    """A sleek white android with a minimal round face plate and a core light."""
    on = s == "working"
    p = ["<defs>" + grad("zero-pearl", "#ffffff", "#bcc4e6") + "</defs>"]
    for x in (15.2, 21.4):
        p.append(f'<rect x="{x}" y="24.6" width="3.4" height="6.6" rx="1.7" fill="url(#zero-pearl)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append('<path d="M23 25.4 H24.2 V29.8 C24.2 30.4 23.6 30.6 23 30.6 Z" fill="#7a5cd6" opacity="0.45"/>')
    for side in (1, -1):
        hx = 20 + side * 8.4
        p.append(cable(f"M{20 + side * 5.6} 18.8 C{20 + side * 7.8} 19.4 {hx} 21 {hx} 25", "url(#zero-pearl)", 2))
        p.append(f'<circle cx="{hx}" cy="25.6" r="1.4" fill="url(#zero-pearl)" stroke="{INK}" stroke-width="1"/>')
    p.append(shape("M14.2 18.8 C14.2 17.8 15 17.2 16 17.2 H24 C25 17.2 25.8 17.8 25.8 18.8 L24.6 25.8 C24.4 26.8 23.6 27.4 22.6 27.4 H17.4 C16.4 27.4 15.6 26.8 15.4 25.8 Z", "url(#zero-pearl)"))
    p.append(shade("M23.6 17.6 C24.8 17.6 25.6 18 25.4 19.4 L24.2 25.8 C24 26.6 23.4 27 22.4 27 H21 C22.8 24.6 23.8 21 23.6 17.6 Z"))
    p.append(line("M16.6 24.6 H23.4", "#a87bff", 0.5, 0.7))
    if on:
        p.append(glow(20, 21, 4, "c"))
    p.append(f'<circle cx="20" cy="21" r="1.7" fill="{lit("c", on)}" stroke="{INK}" stroke-width="0.8"/>')
    p.append(f'<rect x="18.4" y="15.8" width="3.2" height="2" fill="#bcc4e6" stroke="{INK}" stroke-width="0.9"/>')
    # The head: a smooth egg with side discs and the dark face plate.
    for side in (1, -1):
        p.append(f'<circle cx="{20 + side * 9.1}" cy="9.4" r="1.7" fill="url(#zero-pearl)" stroke="{INK}" stroke-width="1"/>')
        if on:
            p.append(glow(20 + side * 9.1, 9.4, 1.6, "c"))
        p.append(f'<circle cx="{20 + side * 9.1}" cy="9.4" r="0.6" fill="{lit("c", on)}"/>')
    p.append(shape("M20 1.4 C26 1.4 29.2 5 29.2 9.4 C29.2 13.8 25.6 16.6 20 16.6 C14.4 16.6 10.8 13.8 10.8 9.4 C10.8 5 14 1.4 20 1.4 Z", "url(#zero-pearl)"))
    p.append(shade("M27 4.2 C28.6 5.6 29.2 7.4 29.2 9.4 C29.2 13.8 25.6 16.6 20 16.6 C24.6 15 27.8 11 27 4.2 Z"))
    p.append(highlight("M13.2 5.6 C14.4 3.8 16.2 2.8 18.4 2.6"))
    if on:
        p.append(glow(20, 9.8, 9, "c", ry=6.5, opacity=0.6))
    p.append(f'<ellipse cx="20" cy="9.8" rx="6.6" ry="4.8" fill="none" stroke="{lit("c", on)}" stroke-width="0.5"/>')
    p.append(f'<ellipse cx="20" cy="9.8" rx="5.8" ry="4.1" fill="{INK}"/>')
    p.append('<ellipse cx="20" cy="9.8" rx="5.1" ry="3.4" fill="url(#screen)"/>')
    p.append(eyes(s, [(17.7, 9), (22.3, 9)], "c", 1))
    p.append(mouth(s, 20, 11.6, 1.8, lit("c")))
    p.append(mark(s, 3, 3))
    return "".join(p)


def omega(s: str) -> str:
    """A chunky security mech with broad shoulders, a tiny head and amber belly lights."""
    on = s == "working"
    alarm = s == "blocked"
    p = ["<defs>" + grad("omega-armor", "#7d8ac0", "#2c3256") + grad("omega-plate", "#b8c2ea", "#5e6aa0") + "</defs>"]
    for x in (12, 22.4):
        p.append(f'<rect x="{x + 0.6}" y="24" width="4.4" height="5" fill="#2c3256" stroke="{INK}" stroke-width="{SW}"/>')
        p.append(f'<rect x="{x - 0.8}" y="28.6" width="7.2" height="2.6" rx="1" fill="url(#omega-plate)" stroke="{INK}" stroke-width="{SW}"/>')
    for side in (1, -1):
        ax = 20 + side * 12.8
        p.append(f'<rect x="{ax - 2.2}" y="13" width="4.4" height="9" rx="1.8" fill="url(#omega-armor)" stroke="{INK}" stroke-width="{SW}"/>')
        p.append(shape(f"M{ax - 3} 22.6 C{ax - 3} 20.6 {ax + 3} 20.6 {ax + 3} 22.6 V25 C{ax + 3} 26.6 {ax - 3} 26.6 {ax - 3} 25 Z", "url(#omega-plate)"))
        p.append(line(f"M{ax - 1.6} 23.4 V25 M{ax} 23.4 V25 M{ax + 1.6} 23.4 V25", INK, 0.5, 0.6))
    # The torso and the belly lights.
    p.append(shape("M10 10.6 H30 C31.6 10.6 32.1 11.8 31.7 13.4 L29.6 23.8 C29.3 25.4 28 26.4 26.4 26.4 H13.6 C12 26.4 10.7 25.4 10.4 23.8 L8.3 13.4 C7.9 11.8 8.4 10.6 10 10.6 Z", "url(#omega-armor)"))
    p.append(shade("M27.6 11.2 H30 C31.2 11.2 31.4 12.2 31.2 13.4 L29.2 23.6 C28.9 25 28 25.8 26.4 25.8 H25 C27.4 21.6 28.4 16.4 27.6 11.2 Z"))
    p.append(line("M12 14.6 H28", lit("a", on), 0.6))
    p.append(f'<rect x="13.4" y="17.4" width="13.2" height="5.6" rx="1.6" fill="{INK}"/>')
    key = "r" if alarm else "a"
    for x in (16.3, 20, 23.7):
        if on or alarm:
            p.append(glow(x, 20.2, 2.6, key))
        p.append(f'<circle cx="{x}" cy="20.2" r="1.25" fill="{lit(key, on or alarm)}"/>')
        p.append(f'<circle cx="{x - 0.4}" cy="19.8" r="0.35" fill="#ffffff" opacity="{0.9 if on or alarm else 0.3}"/>')
    # Big shoulder pads with an amber trim.
    for side in (1, -1):
        cx = 20 + side * 11.6
        p.append(shape(f"M{cx - 6} 12.6 C{cx - 6} 9 {cx - 3} 7.6 {cx} 7.6 C{cx + 3} 7.6 {cx + 6} 9 {cx + 6} 12.6 C{cx + 6} 15.4 {cx + 3} 16.4 {cx} 16.4 C{cx - 3} 16.4 {cx - 6} 15.4 {cx - 6} 12.6 Z", "url(#omega-plate)"))
        p.append(line(f"M{cx - 5} 14 Q{cx} 16.6 {cx + 5} 14", lit("a", on), 0.7))
        p.append(highlight(f"M{cx - 4.4} 11 C{cx - 3.8} 9.4 {cx - 2.4} 8.6 {cx - 0.8} 8.4"))
    p.append(shade("M35.6 10.2 C37 11.4 37.6 12.4 37.6 12.6 C37.6 15.4 34.6 16.4 31.6 16.4 C34 15.2 35.8 13 35.6 10.2 Z"))
    # The tiny head with a visor and a beacon on top.
    if on or alarm:
        p.append(glow(20, 2.8, 2.6, key))
    p.append(f'<rect x="18.9" y="1.6" width="2.2" height="2.6" rx="1" fill="{lit(key, on or alarm)}" stroke="{INK}" stroke-width="0.7"/>')
    p.append(shape("M20 3.8 C23.2 3.8 24.8 5.8 24.8 8.2 C24.8 10.6 23 12.2 20 12.2 C17 12.2 15.2 10.6 15.2 8.2 C15.2 5.8 16.8 3.8 20 3.8 Z", "url(#omega-plate)"))
    p.append(f'<rect x="16" y="6.2" width="8" height="3.2" rx="1.6" fill="{INK}"/>')
    p.append(eyes(s, [(18.2, 7.8), (21.8, 7.8)], "a", 0.8))
    p.append(mouth(s, 20, 10.7, 1.6))
    p.append(mark(s, 2, 1))
    return "".join(p)


def ghost(s: str) -> str:
    """A net ghost with scanline stripes through its body and a wavy hem."""
    on = s == "working"
    hem = "".join(f" Q{x - 2.5} 33 {x - 5} 29.4" for x in (32.5, 27.5, 22.5, 17.5, 12.5))
    body = "M7.5 14 C7.5 6.6 13 2 20 2 C27 2 32.5 6.6 32.5 14 V29.4" + hem + " Z"
    p = ["<defs>" + grad("ghost-body", "#e0fcff", "#4ab4ec") + f'<clipPath id="ghost-clip"><path d="{body}"/></clipPath></defs>']
    if on:
        p.append(glow(20, 16, 17, "c", ry=15, opacity=0.5))
    for side in (1, -1):
        ay = 15.6 if on and side > 0 else 19
        p.append(shape(f"M{20 + side * 11.5} {ay - 1.6} C{20 + side * 15.4} {ay - 2.8} {20 + side * 15.4} {ay + 1.8} {20 + side * 11.5} {ay + 1.6} Z", "url(#ghost-body)"))
    p.append(shape(body, "url(#ghost-body)"))
    # Scanlines, clipped to the body: faint when calm, neon when working.
    p.append('<g clip-path="url(#ghost-clip)">')
    for i, y in enumerate(range(5, 31, 3)):
        if on:
            p.append(f'<rect x="7" y="{y}" width="26" height="0.9" fill="{lit("m" if i % 2 else "c")}" opacity="0.55"/>')
        else:
            p.append(f'<rect x="7" y="{y}" width="26" height="0.9" fill="#1f6aa8" opacity="0.22"/>')
    p.append(shade("M28.4 5.4 C31.2 7.6 32.5 10.6 32.5 14 V31.6 L27.4 31.6 C29.6 23 30.2 12 28.4 5.4 Z"))
    p.append("</g>")
    p.append(f'<path d="{body}" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>')
    p.append(highlight("M10.4 10 C11.6 6.8 14 4.6 17.2 3.8"))
    if on:
        # Glitch bits flying off the body.
        for x, y, k in ((3.6, 9.8, "m"), (35, 22.6, "c"), (2.4, 25, "c"), (36.2, 8.4, "m")):
            p.append(f'<rect x="{x}" y="{y}" width="1.4" height="1.4" fill="{lit(k)}" stroke="{INK}" stroke-width="0.4"/>')
    for cx in (15.6, 24.4):
        p.append(socket(cx, 12.6, 2.4, 2.8))
    p.append(eyes(s, [(15.6, 12.6), (24.4, 12.6)], "c", 1.3))
    p.append(mouth(s, 20, 17.6, 2.6))
    for cx in (12.4, 27.6):
        p.append(f'<ellipse cx="{cx}" cy="16.4" rx="1.4" ry="0.7" fill="#ff7fe0" opacity="0.6"/>')
    p.append(mark(s, 2, 2))
    return "".join(p)


def hydra(s: str) -> str:
    """A three-headed snake made of cables, coiled on the floor."""
    on = s == "working"
    p = ["<defs>" + grad("hydra-scale", "#d8b8ff", "#6a3fc8") + "</defs>"]
    # The coiled cable body: two stacked loops, the necks rising from the top one.
    p.append('<path d="M20 25.4 C27 25.4 31.6 26.6 31.6 28.3 C31.6 30 27 30.9 20 30.9 C13 30.9 8.4 30 8.4 28.3 C8.4 26.6 13 25.4 20 25.4 Z" fill="#4a2a96"/>')
    p.append(cable("M20 25.4 C27 25.4 31.6 26.6 31.6 28.3 C31.6 30 27 30.9 20 30.9 C13 30.9 8.4 30 8.4 28.3 C8.4 26.6 13 25.4 20 25.4 Z", "#7a4ad6", 2.6))
    p.append(line("M23 30.9 C27.6 30.7 31.6 29.8 31.6 28.3", "#4a2a96", 2.6, 0.8))
    p.append(line("M9.4 27.4 C11 26.4 14 25.8 17 25.6", "#ffffff", 0.6, 0.8))
    heads = ((7.4, 11.6, "M14 25.6 C9 23.4 5.6 19.6 7.2 14.4"), (20, 6.4, "M20 24.6 C22.4 19.6 17.6 14.4 20 9.2"), (32.6, 11.6, "M26 25.6 C31 23.4 34.4 19.6 32.8 14.4"))
    for _cx, _cy, d in heads:
        p.append(cable(d, "#8a5ae0", 3))
        p.append(line(d, lit("c", on), 0.5, 1 if on else 0.8))
    p.append('<path d="M20 23.4 C25.4 23.4 28.4 24.4 28.4 25.6 C28.4 26.8 25.4 27.6 20 27.6 C14.6 27.6 11.6 26.8 11.6 25.6 C11.6 24.4 14.6 23.4 20 23.4 Z" fill="#4a2a96"/>')
    p.append(cable("M20 23.4 C25.4 23.4 28.4 24.4 28.4 25.6 C28.4 26.8 25.4 27.6 20 27.6 C14.6 27.6 11.6 26.8 11.6 25.6 C11.6 24.4 14.6 23.4 20 23.4 Z", "#9a6af0", 2.4))
    p.append(line("M12.6 24.8 C14 24 16.4 23.6 18.4 23.5", "#ffffff", 0.6, 0.8))
    for cx, cy, _d in heads:
        if on:
            p.append(glow(cx, cy, 6, "c", ry=5, opacity=0.6))
        p.append(shape(f"M{cx - 5} {cy} C{cx - 5} {cy - 4.2} {cx + 5} {cy - 4.2} {cx + 5} {cy} C{cx + 5} {cy + 3} {cx + 2.6} {cy + 4} {cx} {cy + 4} C{cx - 2.6} {cy + 4} {cx - 5} {cy + 3} {cx - 5} {cy} Z", "url(#hydra-scale)"))
        p.append(shade(f"M{cx + 3.6} {cy - 2.2} C{cx + 4.6} {cy - 1.2} {cx + 5} {cy} {cx + 5} {cy} C{cx + 5} {cy + 3} {cx + 2.6} {cy + 4} {cx} {cy + 4} C{cx + 3} {cy + 2.8} {cx + 4.2} {cy + 0.8} {cx + 3.6} {cy - 2.2} Z"))
        p.append(highlight(f"M{cx - 3.6} {cy - 1.2} C{cx - 3.1} {cy - 2.3} {cx - 2} {cy - 2.9} {cx - 0.8} {cy - 3}"))
        for ex in (cx - 1.9, cx + 1.9):
            p.append(socket(ex, cy - 0.2, 1.45, 1.55))
        p.append(eyes(s, [(cx - 1.9, cy - 0.2), (cx + 1.9, cy - 0.2)], "c", 0.85))
        p.append(mouth(s, cx, cy + 2.4, 1.8))
    p.append(mark(s, 2, 1.5))
    return "".join(p)


def karma(s: str) -> str:
    """A maneki-neko lucky cat robot waving a raised paw and holding a gold coin."""
    on = s == "working"
    p = ["<defs>" + grad("karma-body", "#ffb8ae", "#e04a66") + grad("karma-gold", "#fff2a6", "#e09a14") + "</defs>"]
    p.append(shape("M10.6 31.2 C9.2 26 10.6 19.6 19 19.6 C27.4 19.6 28.8 26 27.4 31.2 Z", "url(#karma-body)"))
    p.append(shade("M24.6 20.4 C28 22.4 28.4 27 27.2 30.6 H22.6 C25 27.6 25.8 23.6 24.6 20.4 Z"))
    # The raised paw: it waves when working.
    turn = -16 if on else 0
    p.append(f'<g transform="rotate({turn} 26 22)">')
    p.append(cable("M25.4 23 C28 20 30.6 16 31.4 12", "#f06a80", 3.2))
    p.append(shape("M31.6 6.4 C33.8 6.4 35.2 8 35.2 10 C35.2 12.2 33.6 13.4 31.6 13.4 C29.6 13.4 28 12.2 28 10 C28 8 29.4 6.4 31.6 6.4 Z", "url(#karma-body)"))
    p.append(f'<ellipse cx="31.6" cy="10.8" rx="1.4" ry="1.1" fill="{lit("m", on)}"/>')
    for x in (30.1, 31.6, 33.1):
        p.append(f'<circle cx="{x}" cy="8.6" r="0.5" fill="{lit("m", on)}"/>')
    p.append("</g>")
    if on:
        p.append(line("M36.2 4.4 Q38 7 37.4 10 M34.6 2.6 Q36 3 37 4", lit("c"), 0.6))
    # The gold coin held to the belly.
    if on:
        p.append(glow(17.4, 25.4, 6.5, "a"))
    p.append(shape("M17.4 21.6 C20.2 21.6 22 23.4 22 25.6 C22 27.8 20.2 29.6 17.4 29.6 C14.6 29.6 12.8 27.8 12.8 25.6 C12.8 23.4 14.6 21.6 17.4 21.6 Z", "url(#karma-gold)"))
    p.append('<ellipse cx="17.4" cy="25.6" rx="3.1" ry="2.7" fill="none" stroke="#b86a10" stroke-width="0.5"/>')
    p.append(f'<rect x="16.5" y="24.7" width="1.8" height="1.8" fill="{INK}"/>')
    p.append(highlight("M14.4 24.4 C14.8 23.4 15.6 22.8 16.4 22.6"))
    p.append(shape("M11.4 23.6 C12.8 22.8 14.4 23.6 14.2 25 C14 26.4 12.4 26.8 11.4 26 Z", "url(#karma-body)", 1))
    # The head, ears and face.
    for side in (1, -1):
        def X(x: float) -> float:
            return 19 + side * (x - 19)
        p.append(shape(f"M{X(10.6)} 8.4 L{X(11.6)} 1.4 L{X(17)} 5 Z", "url(#karma-body)"))
        p.append(f'<path d="M{X(12.1)} 6.6 L{X(12.6)} 3.4 L{X(15.2)} 5.2 Z" fill="url(#karma-gold)"/>')
    p.append(shape("M19 3.8 C25.6 3.8 28 7.6 28 11.6 C28 16.2 24.2 19.2 19 19.2 C13.8 19.2 10 16.2 10 11.6 C10 7.6 12.4 3.8 19 3.8 Z", "url(#karma-body)"))
    p.append(shade("M26.4 7 C27.6 8.4 28 10 28 11.6 C28 16.2 24.2 19.2 19 19.2 C23.8 17.4 27 13 26.4 7 Z"))
    p.append(highlight("M12.6 7.6 C13.8 5.8 15.6 5 17.4 4.8"))
    for cx in (15.6, 22.4):
        p.append(socket(cx, 11.4, 2.2, 2.5))
    p.append(eyes(s, [(15.6, 11.4), (22.4, 11.4)], "a", 1.1))
    p.append(f'<path d="M18.2 14.2 H19.8 L19 15 Z" fill="{lit("m")}" stroke="{INK}" stroke-width="0.4" stroke-linejoin="round"/>')
    p.append(mouth(s, 19, 16.2, 2.4))
    for side in (1, -1):
        x0, x1 = 19 + side * 5.6, 19 + side * 10.4
        p.append(line(f"M{x0} 14.4 L{x1} 13.8 M{x0} 15.6 L{x1} 16.2", lit("c", on), 0.5))
    # The collar with a gold bell.
    p.append(line("M12.6 19.2 C16 20.6 22 20.6 25.4 19.2", INK, 1.6))
    p.append(line("M12.6 19.2 C16 20.6 22 20.6 25.4 19.2", lit("m", on), 0.6))
    p.append(f'<circle cx="19" cy="21" r="1.5" fill="url(#karma-gold)" stroke="{INK}" stroke-width="0.8"/>')
    p.append(line("M19 21.4 V22.4", INK, 0.5))
    p.append(mark(s, 2, 2))
    return "".join(p)


def nitro(s: str) -> str:
    """A turtle with a rocket booster strapped on its shell, the flame lit when working."""
    on = s == "working"
    p = ["<defs>" + grad("nitro-shell", "#ffc874", "#d24e26") + grad("nitro-skin", "#a8f4d6", "#2a9c84") + grad("nitro-rocket", "#ffffff", "#aab4dc") + "</defs>"]
    p.append(shape("M7 26.4 L3.4 27.6 L7.4 28.6 Z", "url(#nitro-skin)", 1))
    for x in (8.6, 22.6):
        p.append(f'<rect x="{x}" y="25" width="4.6" height="6.2" rx="2" fill="url(#nitro-skin)" stroke="{INK}" stroke-width="{SW}"/>')
    # The shell, its rim and plates.
    p.append(shape("M6 25.4 C6 16.6 11.4 11.6 17.8 11.6 C24.2 11.6 29.6 16.6 29.6 25.4 Z", "url(#nitro-shell)"))
    p.append(shade("M24.2 13.8 C27.6 15.8 29.6 19.6 29.6 25.4 H25.4 C26 20.6 25.6 16.8 24.2 13.8 Z"))
    p.append(line("M12.4 25.2 C12.6 20 14.4 16.4 17.8 14.6 C21.2 16.4 23 20 23.2 25.2 M6.6 20.6 H12.8 M22.8 20.6 H29", INK, 0.6, 0.55))
    p.append(f'<rect x="4.6" y="24.2" width="26.4" height="2.8" rx="1.4" fill="#ffe2a8" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(line("M6 25.6 H29.6", lit("a", on), 0.5))
    p.append(highlight("M8.6 19 C9.6 16 11.8 13.6 14.6 12.8"))
    # The neck and head, turned to look at us, with flight goggles.
    p.append(shape("M27 21.6 C28.6 18 30 17.6 31 18.4 L31.6 24.6 C30 25.6 28 25 27 24 Z", "url(#nitro-skin)"))
    p.append(shape("M32.6 14 C35.6 14 37.4 16.2 37.4 18.8 C37.4 21.6 35.4 23.4 32.6 23.4 C29.8 23.4 27.8 21.6 27.8 18.8 C27.8 16.2 29.6 14 32.6 14 Z", "url(#nitro-skin)"))
    p.append(shade("M35.8 15.4 C36.8 16.4 37.4 17.6 37.4 18.8 C37.4 21.6 35.4 23.4 32.6 23.4 C35 22 36.4 19 35.8 15.4 Z"))
    p.append(line("M28 17.4 H37.2", INK, 0.9))
    for cx in (30.8, 34.4):
        p.append(f'<circle cx="{cx}" cy="18" r="1.75" fill="{INK}" stroke="{lit("a", on)}" stroke-width="0.4"/>')
    p.append(eyes(s, [(30.8, 18), (34.4, 18)], "c", 0.95))
    p.append(mouth(s, 32.6, 21.4, 1.8))
    # The rocket booster lying on the shell.
    if on:
        p.append(glow(5, 9.2, 6, "a", ry=4))
        p.append(f'<path d="M8 7 Q3.4 7.2 0.4 9.2 Q3.4 11.2 8 11.4 Z" fill="{lit("a")}" stroke="{INK}" stroke-width="0.6" stroke-linejoin="round"/>')
        p.append(f'<path d="M8 8 Q5 8.4 3.2 9.2 Q5 10 8 10.4 Z" fill="{lit("m")}"/>')
    elif s == "blocked":
        for cx, cy, r in ((5.4, 8.6, 1.3), (3, 7, 1), (1.6, 9.4, 0.8)):
            p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#8a8fa8" stroke="{INK}" stroke-width="0.5" opacity="0.85"/>')
    p.append(shape("M10.4 6.8 L8.6 3.4 H11 L14 6.8 Z", "#ff5a6e", 1))
    p.append(shape("M10 7.6 L7.4 6.8 V11.6 L10 10.8 Z", "url(#metal)", 1))
    p.append(f'<rect x="9.8" y="6.6" width="12.6" height="5.2" rx="1.4" fill="url(#nitro-rocket)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shape("M22 6.6 C25 6.6 27.4 8 27.9 9.2 C27.4 10.4 25 11.8 22 11.8 Z", "#ff5a6e"))
    p.append('<path d="M11 10.2 H22 V11.2 H11 Z" fill="#7a5cd6" opacity="0.45"/>')
    p.append(line("M13.8 6.6 V12.4 M19.6 6.6 V12.4", INK, 0.9))
    key = "r" if s == "blocked" else "a"
    if on or s == "blocked":
        p.append(glow(16.7, 9.2, 2.4, key))
    p.append(f'<circle cx="16.7" cy="9.2" r="1.1" fill="{lit(key, on or s == "blocked")}" stroke="{INK}" stroke-width="0.5"/>')
    p.append(mark(s, 34, 2))
    return "".join(p)


def pulse(s: str) -> str:
    """A frog with a heart-monitor (EKG) screen on its belly."""
    on = s == "working"
    p = ["<defs>" + grad("pulse-skin", "#e2ff86", "#55ac26") + "</defs>"]
    for side in (1, -1):
        p.append(f'<ellipse cx="{20 + side * 11.6}" cy="26.6" rx="4.2" ry="3.8" fill="url(#pulse-skin)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shape("M20 9 C29 9 34 14 34 21.4 C34 27.6 29.4 31.2 20 31.2 C10.6 31.2 6 27.6 6 21.4 C6 14 11 9 20 9 Z", "url(#pulse-skin)"))
    p.append(shade("M30 12.4 C32.6 14.6 34 17.8 34 21.4 C34 27.6 29.4 31 21 31.2 C27.6 28.4 31.4 21.4 30 12.4 Z"))
    p.append(highlight("M9.2 16 C10 14 11.2 12.6 12.8 11.8"))
    # The eye bumps on top of the head.
    for cx in (13, 27):
        p.append(shape(f"M{cx} 4.2 C{cx + 2.8} 4.2 {cx + 4.6} 6 {cx + 4.6} 8.6 C{cx + 4.6} 11.2 {cx + 2.8} 12.8 {cx} 12.8 C{cx - 2.8} 12.8 {cx - 4.6} 11.2 {cx - 4.6} 8.6 C{cx - 4.6} 6 {cx - 2.8} 4.2 {cx} 4.2 Z", "url(#pulse-skin)"))
        p.append(socket(cx, 8.6, 2.6, 2.7))
    p.append(highlight("M9.6 7 C10.2 5.6 11.2 4.9 12.4 4.7"))
    p.append(eyes(s, [(13, 8.6), (27, 8.6)], "g", 1.25))
    p.append(mouth(s, 20, 14.4, 4.2))
    for cx in (11.4, 28.6):
        p.append(f'<ellipse cx="{cx}" cy="15.2" rx="1.5" ry="0.75" fill="#ff7fe0" opacity="0.65"/>')
    # The EKG screen on the belly.
    key = "r" if s == "blocked" else "g"
    p.append(f'<rect x="12.4" y="17.6" width="15.2" height="9.2" rx="2.2" fill="{INK}"/>')
    p.append('<rect x="13.2" y="18.4" width="13.6" height="7.6" rx="1.6" fill="url(#screen)"/>')
    if s == "idle":
        p.append(line("M14 22.4 H18 Q18.8 21.6 19.6 22.4 H26", lit("g", False), 0.6))
    elif s == "done":
        p.append(line("M14 22.4 H16.8 M23.2 22.4 H26", lit("g"), 0.6))
        p.append(glow(20, 22.2, 3.4, "m"))
        p.append(f'<path d="M20 24.6 C17.2 22.8 17 21.4 17.6 20.6 C18.4 19.6 19.6 20 20 20.8 C20.4 20 21.6 19.6 22.4 20.6 C23 21.4 22.8 22.8 20 24.6 Z" fill="{lit("m")}"/>')
    else:
        trace = (
            "M14 22.4 H16.6 L17.4 21.6 L18.2 22.4 L19.2 19.2 L20.4 25.4 L21.4 22.4 H23 L23.8 21.4 L24.6 22.4 H26"
            if on
            else "M14 22.4 L15 20 L16 24.6 L17.2 19.4 L18.4 25.2 L19.6 20.2 L20.8 24.4 L22 19.6 L23.2 25 L24.4 21 L26 22.4"
        )
        p.append(glow(20, 22.2, 7, key, ry=4, opacity=0.6))
        p.append(line(trace, lit(key), 0.6))
    p.append(f'<circle cx="25.6" cy="19.4" r="0.45" fill="{lit(key, s != "idle")}"/>')
    for cx in (14.6, 25.4):
        p.append(shape(f"M{cx - 3} 31.2 C{cx - 3} 29.4 {cx - 1.6} 28.8 {cx} 28.8 C{cx + 1.6} 28.8 {cx + 3} 29.4 {cx + 3} 31.2 Z", "url(#pulse-skin)", 1))
        p.append(line(f"M{cx - 1} 30 V31 M{cx + 1} 30 V31", INK, 0.5, 0.7))
    p.append(mark(s, 1.5, 1))
    return "".join(p)


def wire(s: str) -> str:
    """An octopus made of tangled cables with plug tips."""
    on = s == "working"
    p = ["<defs>" + grad("wire-skin", "#ffc2ee", "#cc3aa2") + "</defs>"]
    # Six cable arms that cross each other, each ending in a plug.
    arms = (
        (13, 5, "M13.4 16.6 C7 17 3.4 21 5 27.4"),
        (19, 11, "M17.4 18.4 C21 21.6 11.6 22.6 11 27.4"),
        (15.6, 16.6, "M14.4 18 C12.6 22 17.4 23 16.6 27.4"),
        (24.4, 23.4, "M25.6 18 C27.4 22 22.6 23 23.4 27.4"),
        (21, 29, "M22.6 18.4 C19 21.6 28.4 22.6 29 27.4"),
        (27, 35, "M26.6 16.6 C33 17 36.6 21 35 27.4"),
    )
    for i, (_sx, x, d) in enumerate(arms):
        p.append(cable(d, "#f07ac8" if i % 2 else "#b8338e", 2))
        if on:
            p.append(glow(x, 28.8, 2.4, "c"))
        p.append(f'<rect x="{x - 1.4}" y="27" width="2.8" height="2.8" rx="0.6" fill="url(#metal)" stroke="{INK}" stroke-width="0.8"/>')
        p.append(f'<rect x="{x - 1}" y="27.9" width="2" height="0.7" fill="{lit("c", on)}"/>')
        p.append(line(f"M{x - 0.6} 30 V31.2 M{x + 0.6} 30 V31.2", "#ffd34d", 0.5))
    # The head: a soft dome with LED spots.
    p.append(shape("M20 2 C27 2 31 6.4 31 11.6 C31 16.4 27.4 19.6 20 19.6 C12.6 19.6 9 16.4 9 11.6 C9 6.4 13 2 20 2 Z", "url(#wire-skin)"))
    p.append(shade("M28 4.6 C30 6.4 31 8.8 31 11.6 C31 16.4 27.4 19.6 20 19.6 C25.6 17.4 29 12 28 4.6 Z"))
    p.append(highlight("M12.2 7 C13.4 4.8 15.4 3.4 17.8 3"))
    for x, y, k in ((17, 5.2, "c"), (20.6, 4.4, "m"), (24, 5.6, "c")):
        if on:
            p.append(glow(x, y, 1.6, k))
        p.append(f'<circle cx="{x}" cy="{y}" r="0.7" fill="{lit(k, on)}" stroke="{INK}" stroke-width="0.4"/>')
    for cx in (16.2, 23.8):
        p.append(socket(cx, 12, 2.4, 2.7))
    p.append(eyes(s, [(16.2, 12), (23.8, 12)], "c", 1.2))
    p.append(mouth(s, 20, 16.4, 2.2))
    for cx in (12.6, 27.4):
        p.append(f'<ellipse cx="{cx}" cy="15.2" rx="1.3" ry="0.65" fill="#ff7fe0" opacity="0.7"/>')
    p.append(mark(s, 2, 2))
    return "".join(p)


SPRITES = {
    "spike": spike,
    "binary": binary,
    "zero": zero,
    "omega": omega,
    "ghost": ghost,
    "hydra": hydra,
    "karma": karma,
    "nitro": nitro,
    "pulse": pulse,
    "wire": wire,
}
