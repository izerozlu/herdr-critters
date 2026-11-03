"""Critters batch B: kilo, vector, relay, daemon, socket, cobalt, rogue, flux, mantis, tesla."""

from .kit import INK, SW, cable, eyes, glow, highlight, line, lit, mark, mouth, shade, shape


def kilo(s: str) -> str:
    """A cargo drone with two rotors, a face screen and a crate under it."""
    on = s == "working"
    p = []
    p.append(cable("M16.5 21 L15.8 24.4 M23.5 21 L24.2 24.4", lit("c", on), 0.5))
    p.append(f'<rect x="13.4" y="24.2" width="13.2" height="7.1" rx="1.2" fill="#ffb347" stroke="{INK}" stroke-width="{SW}"/>')
    p.append('<path d="M22.4 24.8 H26 V30.7 H22.4 Z" fill="#c2562a" opacity="0.55"/>')
    p.append('<rect x="13.4" y="26.4" width="13.2" height="1.5" fill="#2a1d3a"/>')
    p.append(f'<rect x="13.4" y="26.85" width="13.2" height="0.6" fill="{lit("m", on)}"/>')
    p.append(f'<rect x="13.4" y="24.2" width="13.2" height="7.1" rx="1.2" fill="none" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(line("M15.2 29.3 h2.2", INK, 0.6))
    for side in (1, -1):
        hx = 20 + side * 13.2
        p.append(cable(f"M{20 + side * 8} 10.5 L{hx} 6.6", "url(#holoDark)", 0.9))
    for side in (1, -1):
        hx = 20 + side * 13.2
        if on:
            p.append(f'<ellipse cx="{hx}" cy="4.4" rx="5.4" ry="1.5" fill="#9ff4ff" opacity="0.35" stroke="{lit("c")}" stroke-width="0.5"/>')
            p.append(line(f"M{hx - 4.8} 2 Q{hx} 0.4 {hx + 4.8} 2", lit("c"), 0.55))
            p.append(line(f"M{hx - 2.6} 0.9 Q{hx} 0.1 {hx + 2.6} 0.9", lit("m"), 0.5))
        else:
            p.append(cable(f"M{hx - 4.6} 4.6 L{hx + 4.6} 4.0", "#b8b0e0", 0.7))
        p.append(f'<rect x="{hx - 1.5}" y="4.3" width="3" height="3.2" rx="1" fill="url(#holo)" stroke="{INK}" stroke-width="1"/>')
        p.append(f'<circle cx="{hx}" cy="4.4" r="0.75" fill="{INK}"/>')
    if on:
        p.append(glow(20, 14.5, 14, "c", ry=9, opacity=0.6))
    p.append(f'<rect x="9" y="6.6" width="22" height="15" rx="5.2" fill="url(#holo)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M9.7 16.8 C12 19.2 28 19.2 30.3 16.8 C30 19.8 28.2 21 25.8 21 H14.2 C11.8 21 10 19.8 9.7 16.8 Z"))
    p.append(highlight("M11.6 10 C12 8.6 13.2 7.8 14.8 7.6"))
    p.append(line("M20 6.6 V3.8", INK, 0.9))
    if on:
        p.append(glow(20, 3.3, 2, "m"))
    p.append(f'<circle cx="20" cy="3.3" r="0.9" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.6"/>')
    # The face screen, with the eyes and mouth on it.
    p.append(f'<rect x="12" y="9.2" width="16" height="8.8" rx="2.6" fill="{INK}"/>')
    p.append('<rect x="12.9" y="10.1" width="14.2" height="7" rx="1.9" fill="url(#screen)"/>')
    p.append(eyes(s, [(16.6, 13), (23.4, 13)], "c", 1.2))
    p.append(mouth(s, 20, 15.6, 2.2, lit("c")))
    p.append(line("M13.8 11 L15 10.4", "#ffffff", 0.4, 0.5))
    for side, key in ((-1, "m"), (1, "c")):
        cx = 20 + side * 9.7
        if on:
            p.append(glow(cx, 13.6, 1.8, key))
        p.append(f'<circle cx="{cx}" cy="13.6" r="0.6" fill="{lit(key, on)}"/>')
    p.append(line("M14 19.6 H26", lit("m", on), 0.5))
    p.append(mark(s, 1.5, 10))
    return "".join(p)


def lit_brows(s: str, centers: list[tuple[float, float]], r: float, color: str) -> str:
    """Light copies of the kit's blocked brows, so they show on a dark hood or mask."""
    if s != "blocked":
        return ""
    (lx, ly), (rx, ry) = centers[0], centers[-1]
    return line(
        f"M{lx - r * 1.2:.2f} {ly - r * 2.1:.2f} L{lx + r:.2f} {ly - r * 1.5:.2f} "
        f"M{rx + r * 1.2:.2f} {ry - r * 2.1:.2f} L{rx - r:.2f} {ry - r * 1.5:.2f}",
        color,
        0.7,
    )


def vector(s: str) -> str:
    """A wireframe cube robot with glowing neon edges and a face on the front side."""
    on = s == "working"
    edge = lit("g") if on else "#3f9a66"
    p = [
        '<defs><linearGradient id="vector-glass" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#2f7a88"/><stop offset="1" stop-color="#0f2c3c"/></linearGradient></defs>'
    ]
    # Arms: raised when working.
    hy = 15.5 if on else 24.5
    p.append(cable(f"M7.5 20 C5 20 3.6 21.5 3.6 {hy}", "url(#metal)", 1.1))
    p.append(cable(f"M32.5 15 C35 15 36.4 16.5 36.4 {hy - 3}", "url(#metal)", 1.1))
    for hx, y in ((3.6, hy), (36.4, hy - 3)):
        p.append(f'<circle cx="{hx}" cy="{y}" r="1.4" fill="url(#holo)" stroke="{INK}" stroke-width="1"/>')
    p.append(cable("M30.5 23 V29.5 M12 27 V29.5 M21 27 V29.5", "url(#metal)", 1.2))
    for fx in (12, 21, 30.5):
        p.append(f'<rect x="{fx - 2.3}" y="29.4" width="4.6" height="1.9" rx="0.95" fill="url(#holoDark)" stroke="{INK}" stroke-width="1"/>')
    if on:
        p.append(glow(20, 16.5, 18, "g", ry=14, opacity=0.55))
    # Back edges show through the glass.
    p.append(line("M7 28 L14 22 H33 M14 22 V5", edge, 0.5, 0.45))
    for d, fill in (("M7 11 L14 5 H33 L26 11 Z", "#3a8c96"), ("M26 11 L33 5 V22 L26 28 Z", "#0c2533"), ("M7 11 H26 V28 H7 Z", "url(#vector-glass)")):
        p.append(f'<path d="{d}" fill="{fill}" fill-opacity="0.88" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>')
    p.append(shade("M26 17 V28 H15 C20.5 26.6 24.6 22.6 26 17 Z"))
    p.append(highlight("M9 17 V13 H13"))
    p.append(line("M7 11 H26 V28 H7 Z M7 11 L14 5 H33 L26 11 M33 5 V22 L26 28", edge, 0.6))
    for vx, vy in ((7, 11), (26, 11), (7, 28), (26, 28), (14, 5), (33, 5), (33, 22)):
        p.append(f'<circle cx="{vx}" cy="{vy}" r="0.75" fill="{edge}" stroke="{INK}" stroke-width="0.4"/>')
    p.append(line("M20.5 8 V3", INK, 0.9))
    if on:
        p.append(glow(20.5, 2.6, 2, "m"))
    p.append(f'<circle cx="20.5" cy="2.6" r="0.9" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.6"/>')
    p.append(eyes(s, [(12.5, 18), (20.5, 18)], "g", 1.4))
    p.append(mouth(s, 16.5, 23, 2.6, lit("g")))
    p.append(mark(s, 1.5, 2))
    return "".join(p)


def relay(s: str) -> str:
    """A snail with a satellite dish on its shell and eye-stalk antennas."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="relay-skin" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffe2b4"/><stop offset="1" stop-color="#ff9a5a"/></linearGradient>'
        '<linearGradient id="relay-shell" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ff9ee6"/><stop offset="1" stop-color="#8a3fd6"/></linearGradient></defs>'
    ]
    for x0, x1 in ((8.6, 6.3), (12.4, 13.7)):
        p.append(cable(f"M{x0} 17.5 L{x1} 9", "#ffc58a", 1.2))
    p.append(shape("M3.8 31.2 C3 27.5 3.8 23 5 20 C6.2 17 8 15.6 10.5 15.6 C13.2 15.6 14.8 17.6 15.2 20.8 L15.6 25.6 H31.5 C34.6 25.6 37 28.2 37.4 31.2 Z", "url(#relay-skin)"))
    p.append(shade("M27 27.4 H32 C34.4 27.4 36.2 29 36.6 30.6 H26 Z"))
    p.append(highlight("M6.3 21 C6.8 18.8 8 17.2 9.6 16.8"))
    if on:
        p.append(glow(25, 29.6, 9, "c", ry=2))
    p.append(line("M17.5 29.6 H33", lit("c", on), 0.7))
    # The shell, with a neon spiral.
    p.append(shape("M24.5 9.5 A9 9 0 1 1 24.49 9.5 Z", "url(#relay-shell)"))
    p.append(shade("M30.5 12 C34.5 16 34 24 27.5 27 C24 28.5 20 27.6 18 25.6 C24 27 31.5 22.5 30.5 12 Z"))
    p.append(highlight("M17.8 15 C19 12.4 21.2 10.8 23.8 10.5"))
    if on:
        p.append(glow(25, 19.5, 7, "c", opacity=0.7))
    spiral = "M25 19 C25 17.6 27 17.6 27 19.3 C27 21.6 23.4 22.2 22.3 19.8 C21 17 24 14.4 27.4 15.6 C31 17 31.2 22.6 27.6 24.8 C24 27 18.6 25 17.8 20.4"
    p.append(line(spiral, INK, 1.4) + line(spiral, lit("c", on), 0.6))
    # The dish on a mast, its feed horn sends waves when working.
    p.append(cable("M25 10.2 L23.6 8", "#8a90b8", 0.8))
    p.append(shape("M19.2 3.4 C17.4 7.75 27.6 11.95 29.4 7.6 Z"))
    p.append('<ellipse cx="24.3" cy="5.5" rx="5.5" ry="1.4" transform="rotate(22.4 24.3 5.5)" fill="url(#holoDark)" stroke="#140a26" stroke-width="0.8"/>')
    p.append(line("M19.6 3.8 L25.6 2.2 L29 7.2", INK, 0.45))
    p.append(line("M24.3 5.5 L25.6 2.2", INK, 0.8))
    if on:
        p.append(glow(25.6, 2.2, 2.2, "m"))
        p.append(line("M28 0.8 Q29.3 2 28.7 3.7 M30 0.3 Q32 2.4 30.8 4.8", lit("c"), 0.55))
    p.append(f'<circle cx="25.6" cy="2.2" r="0.85" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.6"/>')
    # Eyes on the stalk tips, mouth on the head.
    for cx in (6.3, 13.7):
        p.append(f'<circle cx="{cx}" cy="8.5" r="2.5" fill="url(#holo)" stroke="{INK}" stroke-width="1"/>')
    p.append(eyes(s, [(6.3, 8.5), (13.7, 8.5)], "c", 1.1))
    p.append(f'<ellipse cx="13.2" cy="21.2" rx="1.1" ry="0.6" fill="#ff6fb8" opacity="0.6"/>')
    p.append(mouth(s, 10.4, 22.6, 2.2))
    p.append(mark(s, 34.5, 9))
    return "".join(p)


def daemon(s: str) -> str:
    """A hooded hacker imp with small horns, a laptop and glowing eyes in the hood."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="daemon-hood" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ff6f8e"/><stop offset="1" stop-color="#9a1d4a"/></linearGradient></defs>'
    ]
    p.append(cable("M26.5 28.5 C31 29.5 34.6 27 34.6 22.5 C34.6 20 35.4 18.8 36.6 18.4", "#c22a55", 1.2))
    p.append(shape("M37 14.4 C38.3 15.9 39.3 17.5 38.7 18.8 C37.9 18.3 37.2 18.3 36.6 18.8 C35.7 17.7 35.9 15.9 37 14.4 Z", "url(#daemon-hood)", 1))
    p.append(shape("M11.5 31.2 C11 26 13.5 21.5 20 21.5 C26.5 21.5 29 26 28.5 31.2 Z", "url(#daemon-hood)"))
    p.append(shade("M25 22.4 C27.6 23.8 28.6 27 28.2 30.6 H23.8 C25.2 28 25.6 25 25 22.4 Z"))
    p.append(shape("M20 3.4 C27.6 3.4 31.6 9 31.6 15 C31.6 20.4 27.6 23.4 20 23.4 C12.4 23.4 8.4 20.4 8.4 15 C8.4 9 12.4 3.4 20 3.4 Z", "url(#daemon-hood)"))
    p.append(shade("M30.8 16.5 C30 21 26 22.8 20 22.8 C17 22.8 14.8 22.4 13.2 21.6 C17 22 26.5 22.5 30.8 16.5 Z"))
    p.append(highlight("M11.4 10 C12.6 7.6 14.8 5.6 17.6 5"))
    # Curved horns poke out of the hood.
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(13.6)} 7 C{X(11.2)} 5.6 {X(9.8)} 3.2 {X(9.8)} 0.6 C{X(12.4)} 1.8 {X(14.8)} 3.4 {X(16.6)} 5.4 Z", "#f4e4ff", 1))
        p.append(f'<path d="M{X(9.8)} 0.6 C{X(10.8)} 1.1 {X(11.8)} 1.7 {X(12.6)} 2.4 L{X(10.4)} 2.8 Z" fill="{lit("m", on)}"/>')
    # The dark face in the hood, a neon rim around it.
    p.append(line("M20 7.3 C26.2 7.3 28.7 11.2 28.7 15 C28.7 19.2 25.3 21.5 20 21.5 C14.7 21.5 11.3 19.2 11.3 15 C11.3 11.2 13.8 7.3 20 7.3 Z", lit("m", on), 0.6))
    p.append(shape("M20 8.2 C25.4 8.2 27.8 11.6 27.8 15 C27.8 18.6 24.8 20.6 20 20.6 C15.2 20.6 12.2 18.6 12.2 15 C12.2 11.6 14.6 8.2 20 8.2 Z", "#1d0f2c", 1))
    if on:
        p.append(glow(20, 14.5, 8, "g", ry=6, opacity=0.5))
    centers = [(16.5, 13.8), (23.5, 13.8)]
    p.append(eyes(s, centers, "g", 1.3))
    p.append(lit_brows(s, centers, 1.3, "#ff9ab0"))
    p.append(mouth(s, 20, 17.6, 2.4, "#ffd0e0"))
    p.append(line("M17.4 21.2 V24 M22.6 21.2 V24", INK, 0.6))
    # A laptop on the lap, a code glyph on its lid.
    p.append(f'<rect x="13.4" y="24.6" width="13.2" height="6.6" rx="1" fill="url(#metal)" stroke="{INK}" stroke-width="{SW}"/>')
    if on:
        p.append(glow(20, 27.9, 4.5, "g"))
    p.append(line("M18.3 26.6 L16.8 27.9 L18.3 29.2 M21.7 26.6 L23.2 27.9 L21.7 29.2", lit("g", on), 0.7))
    for cx in (13.6, 26.4):
        p.append(f'<circle cx="{cx}" cy="27.6" r="1.4" fill="url(#daemon-hood)" stroke="{INK}" stroke-width="1"/>')
    p.append(mark(s, 2, 4))
    return "".join(p)


def socket(s: str) -> str:
    """A pink pig with a power socket snout and a curly cord tail with a plug."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="socket-skin" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffc8e4"/><stop offset="1" stop-color="#ff5fa8"/></linearGradient></defs>'
    ]
    p.append(cable("M32 23 C35 23.5 36.6 21.5 35.6 19.8 C34.8 18.4 33 19.4 33.8 20.6 C34.6 21.8 37 20.6 37 17.5 V15", "#ff8ec4", 1))
    p.append(line("M36.3 11.6 V9.4 M37.7 11.6 V9.4", INK, 1.1) + line("M36.3 11.4 V9.6 M37.7 11.4 V9.6", "#e6e8f6", 0.5))
    p.append(f'<rect x="35.4" y="11.2" width="3.2" height="4.2" rx="0.8" fill="url(#metal)" stroke="{INK}" stroke-width="1"/>')
    if on:
        p.append(glow(37, 13.4, 2, "a"))
    p.append(f'<circle cx="37" cy="13.4" r="0.55" fill="{lit("a", on)}"/>')
    for lx in (12.6, 27.4):
        p.append(f'<rect x="{lx - 1.9}" y="25.5" width="3.8" height="5.8" rx="1.3" fill="url(#socket-skin)" stroke="{INK}" stroke-width="{SW}"/>')
        p.append(f'<rect x="{lx - 1.9}" y="29.6" width="3.8" height="1.7" rx="0.7" fill="#8a2f62" stroke="{INK}" stroke-width="0.8"/>')
    p.append(shape("M20 8.6 C28.5 8.6 33.4 13.6 33.4 20 C33.4 26 28 29.6 20 29.6 C12 29.6 6.6 26 6.6 20 C6.6 13.6 11.5 8.6 20 8.6 Z", "url(#socket-skin)"))
    p.append(shade("M32.8 21.5 C31.8 26.6 26.8 29 20 29 C17 29 14.6 28.6 12.6 27.8 C19 28.4 29.5 27.4 32.8 21.5 Z"))
    p.append(highlight("M9.8 15 C11 12.4 13.6 10.4 16.6 9.8"))
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(10)} 13.2 C{X(8.8)} 9.4 {X(9.4)} 6 {X(11)} 4 C{X(13.8)} 5.2 {X(16.4)} 7.6 {X(17.2)} 10 Z", "url(#socket-skin)"))
        p.append(f'<path d="M{X(11.2)} 11.3 C{X(10.6)} 9 {X(10.9)} 7 {X(11.8)} 5.9 C{X(13.6)} 6.9 {X(15)} 8.3 {X(15.6)} 9.8 Z" fill="#ff3f8e" opacity="0.6"/>')
    if on:
        p.append(glow(20, 11.6, 1.8, "g"))
    p.append(f'<circle cx="20" cy="11.6" r="0.7" fill="{lit("g", on)}" stroke="{INK}" stroke-width="0.4"/>')
    p.append(eyes(s, [(15, 14.6), (25, 14.6)], "c", 1.2))
    for cx in (11.6, 28.4):
        p.append(f'<ellipse cx="{cx}" cy="18.6" rx="1.4" ry="0.8" fill="#ff3f8e" opacity="0.45"/>')
    # The socket snout: a face plate with two round holes.
    if on:
        p.append(glow(20, 20.6, 7.5, "c", ry=5.5))
    p.append(shape("M20 16.6 C24.4 16.6 26.2 18.4 26.2 20.6 C26.2 22.9 24.2 24.6 20 24.6 C15.8 24.6 13.8 22.9 13.8 20.6 C13.8 18.4 15.6 16.6 20 16.6 Z", "#fff0f7"))
    p.append(f'<ellipse cx="20" cy="20.6" rx="4.2" ry="2.8" fill="#e8dcef" stroke="{lit("c", on)}" stroke-width="0.6"/>')
    for hx in (18.1, 21.9):
        p.append(f'<circle cx="{hx}" cy="20.6" r="0.95" fill="{INK}"/>')
        if on:
            p.append(f'<circle cx="{hx}" cy="20.6" r="0.45" fill="{lit("c")}"/>')
    p.append(line("M19.4 18.3 H20.6 M19.4 22.9 H20.6", "#a89ab8", 0.6))
    p.append(mouth(s, 20, 26.4, 2.2))
    p.append(mark(s, 2, 3))
    return "".join(p)


def cobalt(s: str) -> str:
    """A blue armored mech beetle with a chrome horn and a visor."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="cobalt-shell" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#8fd4ff"/><stop offset="0.5" stop-color="#2f66e0"/><stop offset="1" stop-color="#1a2a8a"/></linearGradient></defs>'
    ]
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(cable(f"M{X(8.6)} 21 L{X(4)} 22.6 L{X(2.6)} 26.6 M{X(11)} 26 L{X(7.4)} 28.6 L{X(6.6)} 31", "#3f5ad0", 0.9))
    p.append(shape("M20 6.4 C28.6 6.4 34 11.6 34 18.6 C34 25 28 29.4 20 29.4 C12 29.4 6 25 6 18.6 C6 11.6 11.4 6.4 20 6.4 Z", "url(#cobalt-shell)"))
    p.append(shade("M33.4 20 C32.4 25.8 27 28.8 20 28.8 C16.6 28.8 13.8 28.2 11.6 27 C18.6 28 29.6 26.2 33.4 20 Z"))
    p.append(highlight("M9.4 12.4 C11 9.6 13.6 7.8 16.6 7.2"))
    p.append(line("M20 6.6 V15", INK, 1))
    if on:
        p.append(glow(9, 17, 4, "c") + glow(31, 17, 4, "c"))
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        trim = f"M{X(8.4)} 19.5 C{X(8.4)} 13.6 {X(12)} 9.6 {X(17.4)} 8.8"
        p.append(line(trim, INK, 1.4) + line(trim, lit("c", on), 0.6))
        p.append(f'<circle cx="{X(9.6)}" cy="23" r="0.8" fill="{lit("c", on)}" stroke="{INK}" stroke-width="0.5"/>')
    # The horn, then the head with a visor.
    if on:
        p.append(glow(20.4, 2.4, 3, "m"))
    p.append(shape("M16.8 16 C16.4 11.4 17.2 7 18.8 3.6 L17.4 1.2 L20.4 2.4 L23.2 0.8 L22.2 4.4 C21.2 7.8 21.4 11.6 23.2 16 Z"))
    p.append(line("M19.2 14.6 C18.9 11 19.2 7.6 20.4 4.6", lit("m", on), 0.6))
    p.append(shape("M20 14.2 C25.6 14.2 28.6 17.6 28.6 22.2 C28.6 26.6 25 29.6 20 29.6 C15 29.6 11.4 26.6 11.4 22.2 C11.4 17.6 14.4 14.2 20 14.2 Z", "url(#metal)"))
    p.append(highlight("M13.4 18.4 C14.2 16.6 15.6 15.6 17.4 15.2"))
    if on:
        p.append(glow(20, 21, 9, "c", ry=4))
    p.append(f'<rect x="12.8" y="18.6" width="14.4" height="4.8" rx="2.4" fill="{INK}"/>')
    p.append(eyes(s, [(16.4, 21), (23.6, 21)], "c", 1.2))
    p.append(mouth(s, 20, 25.8, 2.2, "#dce6ff"))
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(15)} 28.4 C{X(14.6)} 30 {X(15.6)} 31.2 {X(17.6)} 31.2 C{X(17)} 30.4 {X(17)} 29.6 {X(17.4)} 28.8 Z", "url(#holo)", 0.9))
    p.append(mark(s, 34.5, 1.5))
    return "".join(p)


def rogue(s: str) -> str:
    """A raccoon hacker with a neon eye mask, a ringed tail and a tiny cyberdeck."""
    on = s == "working"
    tail = "M25 28.8 C31.5 30.2 37.6 26.4 37.6 19.6 C37.6 15.8 36.2 13 34 11.6 C33.6 15 33 18.2 31.6 21 C30 24 27.4 25.6 24.6 26 Z"
    p = [
        '<defs><linearGradient id="rogue-fur" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#cfc8de"/><stop offset="1" stop-color="#6a6482"/></linearGradient>'
        f'<clipPath id="rogue-tail"><path d="{tail}"/></clipPath></defs>'
    ]
    p.append(shape(tail, "url(#rogue-fur)"))
    p.append('<g clip-path="url(#rogue-tail)">')
    p.append(line("M28.4 22 L30.4 31 M33.6 15.4 L39 16.6 M32 11.4 L38.6 10.6", "#2a2340", 2))
    if on:
        p.append(glow(35, 22.6, 4, "m"))
    p.append(line("M31.6 19.6 L38.6 24.8", lit("m", on), 2))
    p.append("</g>")
    p.append(f'<path d="{tail}" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>')
    p.append(shape("M12.6 31.2 C11.8 26.4 14 22 20 22 C26 22 28.2 26.4 27.4 31.2 Z", "url(#rogue-fur)"))
    p.append('<ellipse cx="20" cy="28" rx="4.4" ry="3.2" fill="#ece6f6"/>')
    p.append(shade("M24.4 22.8 C27 24.2 28 27.4 27.2 30.6 H23 C24.6 28 25 25.4 24.4 22.8 Z"))
    for cx in (16.2, 23.8):
        p.append(f'<ellipse cx="{cx}" cy="30.5" rx="2.3" ry="1.1" fill="#2a2340" stroke="{INK}" stroke-width="1"/>')
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(10.4)} 11 C{X(9.6)} 7.4 {X(10.2)} 4.6 {X(11.8)} 3.2 C{X(14)} 4 {X(16)} 6 {X(16.8)} 7.8 Z", "url(#rogue-fur)"))
        p.append(f'<path d="M{X(11.4)} 9 C{X(11)} 7 {X(11.3)} 5.4 {X(12.1)} 4.6 C{X(13.4)} 5.2 {X(14.5)} 6.3 {X(15)} 7.4 Z" fill="#2a2340"/>')
    p.append(shape("M20 5.5 C27 5.5 31.5 9.5 31.5 13.5 C31.5 15 32 16.5 33 18 C30.5 18.3 29.5 19 28.5 20 C26.5 21.8 23.5 22.6 20 22.6 C16.5 22.6 13.5 21.8 11.5 20 C10.5 19 9.5 18.3 7 18 C8 16.5 8.5 15 8.5 13.5 C8.5 9.5 13 5.5 20 5.5 Z", "url(#rogue-fur)"))
    p.append(shade("M31.4 15.4 C31.8 16.4 32.2 17.2 32.8 17.9 C30.4 18.3 29.5 19 28.5 20 C26.5 21.8 23.5 22.6 20 22.6 C18.4 22.6 16.8 22.4 15.4 22 C22 21.8 29 19.6 31.4 15.4 Z"))
    p.append(highlight("M11 10.4 C12.4 8.2 14.6 6.8 17.2 6.4"))
    p.append('<path d="M19 6.2 C19.6 8 19.6 10.4 20 12.2 C20.4 10.4 20.4 8 21 6.2 Z" fill="#4a4460"/>')
    p.append(shape("M20 16.6 C23.6 16.6 25.4 18.4 25.4 20 C25.4 21.8 23.2 22.6 20 22.6 C16.8 22.6 14.6 21.8 14.6 20 C14.6 18.4 16.4 16.6 20 16.6 Z", "#f4f0fa", 1))
    # The neon mask with the eyes in it.
    mask = "M9.6 14 C12 12 16.4 12.2 20 13.8 C23.6 12.2 28 12 30.4 14 C30 17 27 18 24.6 17.3 C22.6 16.7 21.3 16.3 20 16.9 C18.7 16.3 17.4 16.7 15.4 17.3 C13 18 10 17 9.6 14 Z"
    if on:
        p.append(glow(20, 15, 12, "m", ry=5, opacity=0.6))
    p.append(shape(mask, "#1d1530", 1))
    p.append(line(mask, lit("m", on), 0.5))
    centers = [(15, 15), (25, 15)]
    p.append(eyes(s, centers, "c", 1.1))
    p.append(lit_brows(s, centers, 1.1, "#ffd0f4"))
    p.append(f'<path d="M18.8 18 H21.2 C21.2 19 20.6 19.5 20 19.5 C19.4 19.5 18.8 19 18.8 18 Z" fill="{INK}"/>')
    p.append(mouth(s, 20, 21, 2))
    # A tiny cyberdeck held in both paws.
    p.append(f'<rect x="16.8" y="23.6" width="6.4" height="3.6" rx="0.6" fill="#2a2340" stroke="{INK}" stroke-width="0.9"/>')
    if on:
        p.append(glow(20, 25.4, 3.4, "g"))
    p.append(line("M18 24.8 H22 M18 26 H20.6", lit("g", on), 0.5))
    for cx in (16.6, 23.4):
        p.append(f'<circle cx="{cx}" cy="25.6" r="1.25" fill="#2a2340" stroke="{INK}" stroke-width="0.9"/>')
    p.append(mark(s, 2, 3))
    return "".join(p)


def flux(s: str) -> str:
    """A floating plasma orb drone with two rings and a glow pool under it."""
    on = s == "working"
    p = [
        '<defs><radialGradient id="flux-orb" cx="0.38" cy="0.35" r="0.7">'
        '<stop offset="0" stop-color="#ffffff"/><stop offset="0.3" stop-color="#e2ccff"/>'
        '<stop offset="0.7" stop-color="#a26cf5"/><stop offset="1" stop-color="#5a2fb8"/></radialGradient></defs>'
    ]
    p.append(glow(20, 30.4, 10, "v", ry=1.9, opacity=1 if on else 0.5))
    p.append(f'<ellipse cx="20" cy="30.4" rx="4.6" ry="0.7" fill="{lit("v", on)}" opacity="0.7"/>')
    if on:
        p.append(glow(20, 24.5, 3.6, "c", ry=5))
        p.append(f'<path d="M18 22.4 Q20 30.4 22 22.4 Z" fill="{lit("c")}" opacity="0.8"/>')
    p.append(shape("M17.2 20 H22.8 L21.8 23.2 H18.2 Z", "url(#metal)", 1))
    rings = (("rotate(-12 20 14)", "M5 14 A15 3.8 0 0 {} 35 14", "c"), ("rotate(22 20 13)", "M7.5 13 A12.5 3 0 0 {} 32.5 13", "m"))

    def ring(i: int, sweep: int) -> str:
        t, d, key = rings[i]
        d = d.format(sweep)
        return f'<g transform="{t}">' + line(d, INK, 2.6) + line(d, "url(#metal)", 1.4) + line(d, lit(key, on), 0.5) + "</g>"

    p.append(ring(0, 1) + ring(1, 1))
    line_up = line("M20 4 V1.8", INK, 0.9)
    p.append(line_up)
    if on:
        p.append(glow(20, 12.5, 14, "v", opacity=0.7))
        p.append(glow(20, 1.6, 2, "a"))
    p.append(f'<circle cx="20" cy="1.6" r="0.85" fill="{lit("a", on)}" stroke="{INK}" stroke-width="0.6"/>')
    p.append(f'<circle cx="20" cy="12.5" r="8.6" fill="url(#flux-orb)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M27.6 9.6 C29.6 15 26.4 20.6 20 20.6 C17.6 20.6 15.6 19.8 14.2 18.6 C21.4 20.4 28.4 16.4 27.6 9.6 Z"))
    p.append(highlight("M13.6 9.4 C14.4 7.2 16.2 5.6 18.4 5"))
    p.append(eyes(s, [(16.6, 12), (23.4, 12)], "c", 1.2))
    p.append(mouth(s, 20, 15.4, 2))
    p.append(ring(0, 0) + ring(1, 0))
    p.append(mark(s, 34, 1.5))
    return "".join(p)


def mantis(s: str) -> str:
    """A cyber praying mantis with a green body and chrome blade arms."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="mantis-body" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#d0ff92"/><stop offset="1" stop-color="#36a046"/></linearGradient>'
        '<linearGradient id="mantis-chrome" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#c4ccec"/><stop offset="1" stop-color="#6a7096"/></linearGradient></defs>'
    ]
    p.append(shape("M22 21.5 C27.5 19.6 34 21.4 36.4 26.4 C37.4 28.8 35.6 30.4 31 30.2 C26.6 30 22.6 28 21.6 25 Z", "url(#mantis-body)"))
    p.append(shade("M36.4 27 C36.6 29 35 30 31 29.8 C28 29.6 25.4 28.8 23.6 27.4 C28 28.6 33 28.8 36.4 27 Z"))
    p.append(line("M26.4 21 C28 23.6 28 27 26.4 29.4 M30.8 21.4 C32.4 24 32.4 27.2 31 30", INK, 0.5, 0.5))
    p.append(cable("M18.4 24 L13.8 27.4 L12.8 31.2 M21.6 24 L25.8 27.8 L26.6 31.2", "#36a046", 0.8))
    p.append(shape("M20 15.2 C22.6 15.2 23.6 18 23.6 21.5 C23.6 25.4 22.2 28 20 28 C17.8 28 16.4 25.4 16.4 21.5 C16.4 18 17.4 15.2 20 15.2 Z", "url(#mantis-body)"))
    p.append(shade("M22.4 17 C23.4 18.6 23.6 20.4 23.6 21.5 C23.6 25.4 22.2 28 20 28 C21.6 25.6 22.6 21.4 22.4 17 Z"))
    if on:
        p.append(glow(20, 21.5, 2.4, "c", ry=5))
    p.append(line("M20 18.6 V24.6", INK, 1.4) + line("M20 18.6 V24.6", lit("c", on), 0.6))
    # The head with big compound eyes and antennas.
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(line(f"M{X(18)} 3.8 C{X(17)} 1.8 {X(15.6)} 1 {X(14)} 1", INK, 0.7))
        if on:
            p.append(glow(X(13.6), 1, 1.6, "m"))
        p.append(f'<circle cx="{X(13.6)}" cy="1" r="0.7" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.5"/>')
    p.append(shape("M11.8 6.6 C11.8 4.2 14.2 3.4 20 3.4 C25.8 3.4 28.2 4.2 28.2 6.6 C28.2 9.6 23.8 14 20 14.6 C16.2 14 11.8 9.6 11.8 6.6 Z", "url(#mantis-body)"))
    p.append(shade("M27.6 8.6 C26.4 11 23 14 20 14.6 C19 14.4 18 14 17 13.4 C21 13.6 25.4 11.6 27.6 8.6 Z"))
    for cx in (14.8, 25.2):
        p.append(f'<circle cx="{cx}" cy="7" r="2.7" fill="#f0ffe4" stroke="{INK}" stroke-width="1"/>')
    p.append(highlight("M13 5.4 C13.6 4.6 14.4 4.3 15.2 4.3"))
    p.append(eyes(s, [(14.8, 7), (25.2, 7)], "c", 1.2))
    p.append(mouth(s, 20, 11.4, 1.6))
    # Chrome blade arms with a neon edge.
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(cable(f"M{X(17.6)} 17.6 L{X(11.2)} 14", "url(#mantis-chrome)", 1.3))
        if on:
            p.append(glow(X(12.4), 19.6, 3, "c", ry=6))
        p.append(shape(f"M{X(10.2)} 13 C{X(8)} 17.4 {X(9.6)} 22.4 {X(15.2)} 25.6 C{X(13)} 21.6 {X(12.4)} 18 {X(13.2)} 14.2 Z", "url(#mantis-chrome)"))
        p.append(line(f"M{X(13.2)} 14.2 C{X(12.4)} 18 {X(13)} 21.6 {X(15.2)} 25.6", lit("c", on), 0.55))
        p.append(line(f"M{X(12.8)} 17 L{X(14.2)} 17.4 M{X(12.8)} 19.8 L{X(14.2)} 20.2", INK, 0.5))
        p.append(f'<circle cx="{X(11.2)}" cy="14" r="1.1" fill="url(#metal)" stroke="{INK}" stroke-width="0.7"/>')
    p.append(mark(s, 3, 3))
    return "".join(p)


def tesla(s: str) -> str:
    """An owl with a tesla coil on its head that sparks when working."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="tesla-feather" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffd2a0"/><stop offset="0.5" stop-color="#e0864a"/><stop offset="1" stop-color="#a24c22"/></linearGradient></defs>'
    ]
    for cx in (16.2, 23.8):
        p.append(f'<ellipse cx="{cx}" cy="30.6" rx="2.2" ry="1" fill="#ffb52e" stroke="{INK}" stroke-width="0.9"/>')
    p.append(shape("M20 9.6 C23 9.6 25.6 10 27.6 10.8 L30.6 7.6 C31.4 9.6 31.4 11.6 30.8 13.2 C32.4 15.6 33 18.6 33 21.4 C33 26.8 27.6 30 20 30 C12.4 30 7 26.8 7 21.4 C7 18.6 7.6 15.6 9.2 13.2 C8.6 11.6 8.6 9.6 9.4 7.6 L12.4 10.8 C14.4 10 17 9.6 20 9.6 Z", "url(#tesla-feather)"))
    p.append(shade("M32.6 22.4 C31.8 27 27 29.4 20 29.4 C17.4 29.4 15 29 13 28.2 C20 28.8 29.8 27.6 32.6 22.4 Z"))
    p.append(highlight("M9.6 16 C10.2 14.4 11 13.4 12.2 12.6"))
    p.append('<ellipse cx="20" cy="25.2" rx="6.2" ry="4.2" fill="#ffe2bf"/>')
    p.append(line("M17.4 23.8 L18.4 24.6 L19.4 23.8 M20.6 23.8 L21.6 24.6 L22.6 23.8 M19 26.6 L20 27.4 L21 26.6", "#c0652e", 0.5))
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(8.8)} 17 C{X(6.4)} 20 {X(6.2)} 25.4 {X(9.4)} 28.4 C{X(11.2)} 26.8 {X(12.2)} 23.4 {X(11.8)} 19.6 Z", "#a24c22"))
        p.append(line(f"M{X(8.6)} 21 C{X(8.4)} 23.4 {X(8.8)} 25.4 {X(9.8)} 26.8", lit("c", on), 0.5))
    for cx in (15.4, 24.6):
        p.append(f'<circle cx="{cx}" cy="16.6" r="4.5" fill="#fff2dc" stroke="{INK}" stroke-width="1"/>')
    p.append(eyes(s, [(15.4, 16.6), (24.6, 16.6)], "c", 1.5))
    p.append(shape("M18.8 19.8 H21.2 L20 22.2 Z", "#ffb52e", 0.8))
    p.append(mouth(s, 20, 23.2, 2))
    # The tesla coil: a copper winding with a chrome ring on top.
    p.append(f'<rect x="16.6" y="8.4" width="6.8" height="1.8" rx="0.7" fill="url(#metal)" stroke="{INK}" stroke-width="1"/>')
    if on:
        p.append(glow(20, 5.8, 4, "c", ry=4))
    p.append(f'<rect x="18.2" y="4" width="3.6" height="4.6" rx="0.6" fill="#e0864a" stroke="{INK}" stroke-width="1"/>')
    p.append(line("M18.4 5.4 H21.6 M18.4 6.6 H21.6 M18.4 7.8 H21.6", lit("c") if on else "#7a3a1a", 0.45))
    if on:
        p.append(glow(20, 3, 8, "c", ry=4))
        bolts = "M16.2 2.8 L14 1.4 L12.8 3.2 L10.6 2 M23.8 2.8 L26 1.2 L27.2 3.2 L29.4 2.2"
        p.append(line(bolts, INK, 1.3) + line(bolts, lit("c"), 0.6))
    p.append(f'<ellipse cx="20" cy="3.2" rx="4" ry="1.6" fill="url(#holo)" stroke="{INK}" stroke-width="1"/>')
    p.append(highlight("M17.4 2.6 Q18.6 2 20 2"))
    p.append(mark(s, 2, 2))
    return "".join(p)


SPRITES = {
    "kilo": kilo,
    "vector": vector,
    "relay": relay,
    "daemon": daemon,
    "socket": socket,
    "cobalt": cobalt,
    "rogue": rogue,
    "flux": flux,
    "mantis": mantis,
    "tesla": tesla,
}
