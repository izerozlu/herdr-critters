"""Critters batch A: glitch, proxy, cipher, vapor, razor, chrome, neon, static, synth, shard."""

from .kit import INK, SW, cable, eyes, glow, highlight, line, lit, mark, mouth, shade, shape


def glitch(s: str) -> str:
    """A glitch slime blob with RGB-split edges and pixel chunks breaking off."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="glitch-body" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#d6ff8a"/><stop offset="1" stop-color="#2fcf7a"/></linearGradient></defs>'
    ]
    body = (
        "M7.4 31.2 C6.4 25.4 7.8 19.6 10.8 15 C13.4 11 16.6 8.6 20 8.6 C23.4 8.6 26.6 11 29.2 15 "
        "C32.2 19.6 33.6 25.4 32.6 31.2 Z"
    )
    if on:
        p.append(glow(20, 21, 16, "g", ry=12, opacity=0.5))
    # The RGB split: a magenta and a cyan copy of the body, offset left and right.
    dx = 1.7 if on else 1
    p.append(f'<path d="{body}" fill="{lit("m")}" opacity="0.85" transform="translate({-dx} -0.4)"/>')
    p.append(f'<path d="{body}" fill="{lit("c")}" opacity="0.85" transform="translate({dx} 0.4)"/>')
    p.append(shape(body, "url(#glitch-body)"))
    p.append(shade("M26.6 13.4 C30.4 18 32.4 24.4 31.8 30.6 H25.4 C28.4 25.4 28.8 19 26.6 13.4 Z"))
    p.append(highlight("M11.4 17.6 C12.8 13.8 15.4 11.2 18.2 10.4"))
    p.append(line("M10.6 23.6 H13.6 M27.2 26.6 H30", "#1f8a5a", 0.6, 0.6))
    # A torn slice of the body, shifted sideways.
    sx = 3.2 if on else 1.4
    p.append(f'<rect x="{22 + sx}" y="21.2" width="9.4" height="1.9" fill="url(#glitch-body)" stroke="{INK}" stroke-width="0.6"/>')
    p.append(f'<rect x="{22 + sx + 9.4}" y="21.2" width="1.2" height="1.9" fill="{lit("c")}"/>')
    # Pixel chunks breaking off the top right.
    for x, y, w in ((30.4, 10.2, 2.6), (33.6, 6.8, 1.9), (31.6, 3.6, 1.3)):
        if on:
            p.append(f'<rect x="{x - 0.6}" y="{y}" width="{w}" height="{w}" fill="{lit("m")}" opacity="0.8"/>')
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" fill="#c8ff7a" stroke="{INK}" stroke-width="0.6"/>')
    p.append(eyes(s, [(16, 19.4), (24, 19.4)], "m", 1.3))
    p.append(mouth(s, 20, 23.6, 2.6))
    for cx in (12.8, 27.2):
        p.append(f'<ellipse cx="{cx}" cy="22.4" rx="1.3" ry="0.7" fill="#ff7fe0" opacity="0.6"/>')
    p.append(mark(s, 2.5, 3))
    return "".join(p)


def proxy(s: str) -> str:
    """A small android with a wide visor over the eyes and a headset antenna."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="proxy-body" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#fff38a"/><stop offset="1" stop-color="#ffb02e"/></linearGradient></defs>'
    ]
    for cx in (16.4, 23.6):
        p.append(f'<rect x="{cx - 1}" y="27" width="2" height="3" fill="url(#metal)" stroke="{INK}" stroke-width="0.8"/>')
        p.append(f'<ellipse cx="{cx}" cy="30.5" rx="2.5" ry="1.1" fill="url(#metal)" stroke="{INK}" stroke-width="1"/>')
    for side in (1, -1):
        p.append(cable(f"M{20 + side * 6.4} 22.4 L{20 + side * 9.4} 26.2", "url(#metal)", 1))
        p.append(f'<circle cx="{20 + side * 9.6}" cy="26.6" r="1.3" fill="url(#proxy-body)" stroke="{INK}" stroke-width="0.9"/>')
    p.append(shape("M14 20 H26 C27 20 27.6 20.8 27.4 21.8 L26.6 27.4 C26.4 28.4 25.8 28.8 24.8 28.8 H15.2 C14.2 28.8 13.6 28.4 13.4 27.4 L12.6 21.8 C12.4 20.8 13 20 14 20 Z", "url(#proxy-body)"))
    p.append(shade("M24.6 20.6 H26.4 C27 21 27 21.6 26.8 22.4 L26.2 27.2 C26 28 25.6 28.2 24.8 28.2 H22.8 C24.4 25.8 25 23 24.6 20.6 Z"))
    p.append(f'<rect x="16.8" y="22" width="6.4" height="3.6" rx="1" fill="{INK}"/>')
    for i, key in enumerate("mca"):
        cx = 18.2 + i * 1.8
        if on:
            p.append(glow(cx, 23.8, 1.6, key))
        p.append(f'<circle cx="{cx}" cy="23.8" r="0.6" fill="{lit(key, on)}"/>')
    # The antenna rises from the right earcup.
    p.append(line("M31.2 11 L33.6 2.8", INK, 0.9))
    if on:
        p.append(glow(33.8, 2.2, 2, "m"))
    p.append(f'<circle cx="33.8" cy="2.2" r="1" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.6"/>')
    p.append(f'<rect x="9.6" y="4.8" width="20.8" height="15.8" rx="6.4" fill="url(#proxy-body)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M10.4 16.4 C13 18.8 27 18.8 29.6 16.4 C29.2 18.8 27.4 20 24.4 20 H15.6 C12.6 20 10.8 18.8 10.4 16.4 Z"))
    p.append(highlight("M12.4 8.4 C13.2 7 14.6 6.2 16.4 6"))
    # The wide visor, the eyes on its glass.
    if on:
        p.append(glow(20, 12.8, 13, "c", ry=5, opacity=0.8))
    p.append(f'<rect x="8.6" y="9.4" width="22.8" height="6.6" rx="3.3" fill="{INK}"/>')
    p.append('<rect x="9.8" y="10.4" width="20.4" height="4.6" rx="2.3" fill="url(#screen)"/>')
    if on:
        p.append(line("M11.4 11.2 H28.6", lit("c"), 0.35, 0.6))
    p.append(eyes(s, [(15.6, 12.7), (24.4, 12.7)], "c", 1.2))
    p.append(line("M11 11.2 L12.4 10.8", "#ffffff", 0.4, 0.5))
    p.append(mouth(s, 20, 17.9, 2.4))
    # The headset: two earcups and a mic boom.
    for cx in (9.2, 30.8):
        p.append(f'<circle cx="{cx}" cy="12.8" r="2.6" fill="url(#metal)" stroke="{INK}" stroke-width="1"/>')
        p.append(f'<circle cx="{cx}" cy="12.8" r="1.1" fill="{lit("c", on)}"/>')
    p.append(cable("M9.6 15.2 C10 17.4 12.4 18.4 14.8 18.2", "url(#metal)", 0.7))
    p.append(f'<circle cx="15.2" cy="18.2" r="0.85" fill="{lit("m", on)}" stroke="{INK}" stroke-width="0.5"/>')
    p.append(mark(s, 2, 2))
    return "".join(p)


def cipher(s: str) -> str:
    """A cyborg cat with an amber LED visor, ear antennas and a cable tail."""
    on = s == "working"
    p = []
    tail = "M27.5 28.5 C33 29 35.5 25 34.5 20.5 C34 18 35 16.5 36.2 16"
    p.append(cable(tail, "url(#holoDark)", 1.7))
    if on:
        p.append(glow(36.4, 14.6, 3, "c"))
    p.append(f'<rect x="35" y="13" width="2.8" height="3.4" rx="0.7" fill="#2a2450" stroke="{INK}" stroke-width="1"/>')
    p.append(line("M35.9 13 v-1.3 M36.9 13 v-1.3", INK, 0.7))
    p.append(f'<rect x="35.7" y="14.2" width="1.4" height="0.9" rx="0.3" fill="{lit("c", on)}"/>')
    p.append(shape("M12.6 31.2 C11.6 26.5 13.5 21 20 21 C26.5 21 28.4 26.5 27.4 31.2 Z"))
    p.append(shade("M23.5 21.8 C26.8 23.2 27.9 27 27.2 30.6 L22.8 30.6 C24.4 27.6 24.6 24.3 23.5 21.8 Z"))
    if on:
        p.append(glow(20, 26.2, 3.2, "m"))
    p.append(line("M18.2 25 L20 27.3 L21.8 25", lit("m", on), 0.8))
    for cx in (16.6, 23.4):
        p.append(f'<ellipse cx="{cx}" cy="30.6" rx="2.4" ry="1.15" fill="url(#holo)" stroke="{INK}" stroke-width="1"/>')
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(10.6)} 10.5 L{X(11.4)} 2.6 L{X(18)} 7 Z"))
        p.append(f'<path d="M{X(12.1)} 8.6 L{X(12.5)} 4.8 L{X(15.8)} 7.2 Z" fill="url(#holoDark)" opacity="0.85"/>')
        key = "m" if side < 0 else "c"
        p.append(line(f"M{X(11.4)} 2.6 L{X(10.2)} 0.9", INK, 0.9))
        if on:
            p.append(glow(X(10.1), 1.1, 1.8, key))
        p.append(f'<circle cx="{X(10.1)}" cy="1.1" r="0.85" fill="{lit(key, on)}" stroke="{INK}" stroke-width="0.6"/>')
    p.append(shape("M20 5.2 C27.5 5.2 30.6 9.2 30.6 13.6 C30.6 18.6 26.4 21.6 20 21.6 C13.6 21.6 9.4 18.6 9.4 13.6 C9.4 9.2 12.5 5.2 20 5.2 Z"))
    p.append(shade("M30 15 C29.2 19 25.6 21 20 21 C17 21 14.8 20.4 13.4 19.4 C16 20 24.5 20.6 30 15 Z"))
    p.append(highlight("M13 9.4 C14.2 7.6 16 6.8 18 6.5"))
    # The visor: a dark band, amber glass when lit, the eyes inside it.
    if on:
        p.append(glow(20, 12.9, 12, "a", ry=5))
    p.append(f'<rect x="10.8" y="10.4" width="18.4" height="5.2" rx="2.6" fill="{INK}"/>')
    p.append(f'<rect x="11.9" y="11.3" width="16.2" height="3.4" rx="1.7" fill="{lit("a", on)}" opacity="{1 if on else 0.8}"/>')
    p.append(eyes(s, [(15.5, 13), (24.5, 13)], "a", 1.1))
    p.append(f'<path d="M19.2 16.7 H20.8 L20 17.6 Z" fill="{lit("m")}" stroke="{INK}" stroke-width="0.4" stroke-linejoin="round"/>')
    p.append(mouth(s, 20, 18.6, 2.4))
    for side in (1, -1):
        x0, x1 = 20 + side * 6.8, 20 + side * 12.6
        p.append(line(f"M{x0} 17 L{x1} 16.2 M{x0} 18.3 L{x1} 18.8", lit("c", on), 0.55))
    for cx in (13.4, 26.6):
        p.append(f'<ellipse cx="{cx}" cy="17.4" rx="1.3" ry="0.7" fill="#ff7fe0" opacity="0.6"/>')
    p.append(mark(s, 2.5, 6))
    return "".join(p)


def vapor(s: str) -> str:
    """A holographic jellyfish drone with a pastel bell and cable tentacles with plug tips."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="vapor-bell" x1="0" y1="0" x2="0.6" y2="1">'
        '<stop offset="0" stop-color="#ffa8e6" stop-opacity="0.95"/><stop offset="0.5" stop-color="#c7a6ff" stop-opacity="0.88"/>'
        '<stop offset="1" stop-color="#86eeff" stop-opacity="0.85"/></linearGradient></defs>'
    ]
    p.append(f'<ellipse cx="20" cy="31" rx="8" ry="0.7" fill="{INK}" opacity="0.25"/>')
    for x0, d in (
        (12.4, "M12.4 19 C8.6 21 13.6 23.6 9.6 26.6"),
        (17, "M17 19.6 C14.6 22.4 19.2 24.4 16 28"),
        (23, "M23 19.6 C25.4 22.4 20.8 24.4 24 28"),
        (27.6, "M27.6 19 C31.4 21 26.4 23.6 30.4 26.6"),
    ):
        p.append(cable(d, "#c9b6ff", 1))
        x, y = float(d.split()[-2]), float(d.split()[-1])
        p.append(line(f"M{x - 0.45} {y + 2} v1.2 M{x + 0.45} {y + 2} v1.2", INK, 0.5))
        if on:
            p.append(glow(x, y + 1.2, 2, "c"))
        p.append(f'<rect x="{x - 1}" y="{y}" width="2" height="2.3" rx="0.5" fill="{lit("c", on)}" stroke="{INK}" stroke-width="0.6"/>')
    if on:
        p.append(glow(20, 12, 15, "m", ry=11, opacity=0.5))
    xs = [7.4 + i * 25.2 / 6 for i in range(7)]
    edge = "".join(f" Q{(a + b) / 2:.2f} 21 {b:.2f} 18.6" for a, b in zip(xs, xs[1:]))
    p.append(shape(f"M32.6 18.6 C32.6 9.6 27 3.6 20 3.6 C13 3.6 7.4 9.6 7.4 18.6{edge} Z", "url(#vapor-bell)"))
    p.append(shade("M27.6 6.6 C30.8 9 32 13.4 32 17.6 C31 19 30 19 28.6 18.4 C29.6 14 29.2 9.6 27.6 6.6 Z"))
    p.append(highlight("M11.4 9.4 C12.8 7 15 5.4 17.6 5"))
    # The inner glow ring of the hologram.
    p.append(line("M11.4 17 C11 11 14.6 7.4 20 7.4 C25.4 7.4 29 11 28.6 17", "#ffffff", 0.5, 0.55))
    if on:
        p.append(glow(20, 5.8, 3, "c"))
    p.append(line("M17.4 5.9 H22.6", lit("c", on), 0.9))
    p.append(eyes(s, [(16, 13), (24, 13)], "v", 1.2))
    p.append(mouth(s, 20, 16, 2.2))
    for cx in (12.8, 27.2):
        p.append(f'<ellipse cx="{cx}" cy="15.4" rx="1.3" ry="0.7" fill="#ff7fe0" opacity="0.6"/>')
    p.append(mark(s, 2.5, 3))
    return "".join(p)


def razor(s: str) -> str:
    """A cyborg fox with chrome blade ears, an orange body and a bushy tail."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="razor-fur" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="#ff5a1f"/></linearGradient>'
        '<linearGradient id="razor-blade" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#ffffff"/><stop offset="0.5" stop-color="#b4bcdc"/><stop offset="1" stop-color="#5a6290"/></linearGradient></defs>'
    ]
    p.append(shape("M25.6 29.8 C31.4 31 37 27.4 37.4 21.4 C37.6 17.8 36 15.4 33.6 15.4 C34.2 19.6 32 23.8 26 25.4 Z", "url(#razor-fur)"))
    p.append(shape("M33.6 15.4 C36 15.4 37.6 17.8 37.4 21.4 C36.2 20.2 34.6 18.6 33.6 15.4 Z", "#fff4ea", 1))
    if on:
        p.append(glow(32, 25.4, 3, "c"))
    p.append(line("M28 27.6 C31 27.2 33.4 25.6 34.6 23", lit("c", on), 0.8))
    p.append(shape("M12.8 31.2 C11.8 26.4 13.8 21.4 20 21.4 C26.2 21.4 28.2 26.4 27.2 31.2 Z", "url(#razor-fur)"))
    p.append(shade("M23.6 22 C26.8 23.4 27.8 27 27 30.6 H22.6 C24.2 27.6 24.6 24.4 23.6 22 Z"))
    p.append('<path d="M16.6 22 Q20 28.6 23.4 22 Z" fill="#fff4ea"/>')
    for cx in (16.6, 23.4):
        p.append(f'<ellipse cx="{cx}" cy="30.6" rx="2.4" ry="1.15" fill="#3d2850" stroke="{INK}" stroke-width="1"/>')
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(11.2)} 10.6 L{X(8.8)} 0.8 L{X(17.6)} 7 Z", "url(#razor-blade)"))
        if on:
            p.append(glow(X(11), 5.4, 2.6, "m"))
        p.append(line(f"M{X(9.8)} 2.6 L{X(11.6)} 9", lit("m", on), 0.8))
    p.append(shape("M20 6.4 C25.6 6.4 29.2 9.2 30.4 13 L33.8 16.4 C30.6 19.8 25.6 22.2 20 22.2 C14.4 22.2 9.4 19.8 6.2 16.4 L9.6 13 C10.8 9.2 14.4 6.4 20 6.4 Z", "url(#razor-fur)"))
    p.append('<path d="M12.6 17 C15.6 16.4 17.6 15.4 20 15.4 C22.4 15.4 24.4 16.4 27.4 17 C25.4 20.2 23 21.6 20 21.6 C17 21.6 14.6 20.2 12.6 17 Z" fill="#fff4ea"/>')
    p.append(shade("M30 15.4 L33 16.6 C30.4 19.4 26 21.4 22 21.9 C25.6 20.4 28.4 18.2 30 15.4 Z"))
    p.append(highlight("M12 11 C13.2 9 15.2 7.8 17.6 7.5"))
    # The cyber implant: a circuit line by the right eye.
    p.append(line("M27.2 10.8 L29 12.4 V15", lit("c", on), 0.6))
    p.append(f'<circle cx="29" cy="15.2" r="0.6" fill="{lit("c", on)}"/>')
    p.append(eyes(s, [(15.6, 12.8), (24.4, 12.8)], "c", 1.2))
    p.append(f'<ellipse cx="20" cy="17" rx="1.2" ry="0.75" fill="{INK}"/>')
    p.append(mouth(s, 20, 19.2, 2.4))
    p.append(mark(s, 2, 4.5))
    return "".join(p)


def chrome(s: str) -> str:
    """A chrome-plated rabbit with long ears and one neon cyber eye."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="chrome-body" x1="0" y1="0" x2="0.5" y2="1">'
        '<stop offset="0" stop-color="#ffffff"/><stop offset="0.38" stop-color="#d4d9ee"/>'
        '<stop offset="0.5" stop-color="#5c6488"/><stop offset="0.58" stop-color="#f2f4ff"/>'
        '<stop offset="1" stop-color="#8a92b6"/></linearGradient></defs>'
    ]
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(15.8)} 10.4 C{X(13.4)} 7 {X(11.8)} 1.2 {X(14)} 0.7 C{X(16.4)} 0.2 {X(18.4)} 6 {X(18.6)} 10 Z", "url(#chrome-body)"))
        if on:
            p.append(glow(X(15.6), 5, 2.4, "m", ry=4))
        p.append(line(f"M{X(14.4)} 2.6 C{X(15)} 4.8 {X(16)} 7 {X(16.6)} 9", lit("m", on), 0.9))
    p.append(shape("M11.8 31.2 C10.6 26 13.2 21 20 21 C26.8 21 29.4 26 28.2 31.2 Z", "url(#chrome-body)"))
    p.append(shade("M24 21.6 C27.4 23 28.6 26.8 27.8 30.6 H23 C24.8 27.6 25.2 24.2 24 21.6 Z"))
    if on:
        p.append(glow(20, 26.6, 3, "c"))
    p.append(f'<rect x="17.4" y="25.6" width="5.2" height="2" rx="1" fill="{INK}"/>')
    p.append(f'<rect x="18.1" y="26.1" width="3.8" height="1" rx="0.5" fill="{lit("c", on)}"/>')
    for cx in (15.4, 24.6):
        p.append(f'<ellipse cx="{cx}" cy="30.6" rx="3" ry="1.15" fill="url(#chrome-body)" stroke="{INK}" stroke-width="1"/>')
    p.append(shape("M20 8.2 C26.2 8.2 30 11.8 30 16 C30 20.2 25.8 22.6 20 22.6 C14.2 22.6 10 20.2 10 16 C10 11.8 13.8 8.2 20 8.2 Z", "url(#chrome-body)"))
    p.append(shade("M29.4 17.4 C28.6 20.6 25 22 20 22 C17.6 22 15.6 21.6 14.2 21 C17 21.2 25 21.4 29.4 17.4 Z"))
    p.append(highlight("M12.6 12.4 C13.8 10.6 15.6 9.6 17.8 9.3"))
    # The cyber eye: a neon monocle ring with a wire to the ear.
    if on:
        p.append(glow(24.4, 15, 4.2, "m"))
    p.append(line("M26.4 13 L28 10.4 L24.6 9.4", lit("m", on), 0.6))
    p.append(f'<circle cx="24.4" cy="15" r="2.6" fill="#ffd0f4" stroke="{INK}" stroke-width="1.6"/>')
    p.append(f'<circle cx="24.4" cy="15" r="2.6" fill="none" stroke="{lit("m", on)}" stroke-width="0.7"/>')
    p.append(eyes(s, [(15.6, 15), (24.4, 15)], "c", 1.15))
    p.append('<path d="M19.2 17.8 H20.8 L20 18.7 Z" fill="#ff7fe0" stroke="#140a26" stroke-width="0.4" stroke-linejoin="round"/>')
    p.append(mouth(s, 20, 19.8, 2.2))
    p.append(f'<ellipse cx="13.4" cy="18.4" rx="1.3" ry="0.7" fill="#ff7fe0" opacity="0.6"/>')
    p.append(mark(s, 2.5, 4))
    return "".join(p)


def neon(s: str) -> str:
    """A moth made of neon sign tubes with a small dark body."""
    on = s == "working"
    p = []
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        upper = f"M{X(18.6)} 12 C{X(14)} 5 {X(8)} 1.6 {X(4.2)} 3 C{X(2.4)} 6.2 {X(4.4)} 12.6 {X(8)} 15.6 C{X(11.6)} 18.2 {X(16)} 17.2 {X(18.6)} 15.4"
        lower = f"M{X(18.6)} 17 C{X(14.6)} 17.2 {X(9.8)} 19.2 {X(8.8)} 22.6 C{X(8.2)} 26 {X(11.4)} 28 {X(14.2)} 26.6 C{X(16.6)} 25.2 {X(18.2)} 21.8 {X(18.8)} 19.4"
        for d, key, cx, cy in ((upper, "m", 10.4, 9.6), (lower, "c", 13.2, 22.4)):
            p.append(f'<path d="{d} Z" fill="#2a1d4a" opacity="0.55"/>')
            if on:
                p.append(glow(X(cx), cy, 7.4, key, ry=6.4, opacity=0.75))
            p.append(cable(d, lit(key, on), 1.1))
        if on:
            p.append(glow(X(9.6), 8.6, 2.6, "a"))
        p.append(f'<circle cx="{X(9.6)}" cy="8.6" r="1.6" fill="none" stroke="{INK}" stroke-width="2.4"/>')
        p.append(f'<circle cx="{X(9.6)}" cy="8.6" r="1.6" fill="none" stroke="{lit("a", on)}" stroke-width="0.9"/>')
        p.append(cable(f"M{X(18.6)} 5.4 C{X(17.6)} 2.6 {X(15.6)} 1.2 {X(13.6)} 1.4", lit("a", on), 0.6))
        p.append(line(f"M{X(19.2)} 27.8 L{X(17.8)} 31", INK, 0.8))
    p.append(shape("M20 10.6 C22.2 10.6 23 13 23 16 C23 21 22 26.6 20 29.6 C18 26.6 17 21 17 16 C17 13 17.8 10.6 20 10.6 Z", "#2a1d4a"))
    p.append(line("M17.6 19.4 H22.4 M17.9 22.6 H22.1 M18.6 25.6 H21.4", lit("v", on), 0.7))
    p.append(highlight("M18.4 13 C18.6 12 19 11.6 19.6 11.4"))
    p.append(shape("M20 4.4 C22.6 4.4 24 6.2 24 8.4 C24 10.8 22.4 12.2 20 12.2 C17.6 12.2 16 10.8 16 8.4 C16 6.2 17.4 4.4 20 4.4 Z", "#d6caff"))
    p.append(shade("M23.4 9.4 C23 11.2 21.6 11.8 20 11.8 C21.8 11.2 23 10.4 23.4 9.4 Z"))
    p.append(eyes(s, [(18.4, 8), (21.6, 8)], "v", 0.85))
    p.append(mouth(s, 20, 10.4, 1.5))
    p.append(mark(s, 1.5, 25.5))
    return "".join(p)


def static(s: str) -> str:
    """A kid in a purple hoodie with a CRT TV for a head; the face is on the screen."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="static-hood" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#c58cff"/><stop offset="1" stop-color="#6a36d6"/></linearGradient>'
        '<linearGradient id="static-tv" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#f4ecd6"/><stop offset="1" stop-color="#b8aa8c"/></linearGradient></defs>'
    ]
    for cx in (16.6, 23.4):
        p.append(f'<rect x="{cx - 1.3}" y="27" width="2.6" height="3" fill="#2a2a5a" stroke="{INK}" stroke-width="0.8"/>')
        p.append(f'<ellipse cx="{cx}" cy="30.5" rx="2.5" ry="1.1" fill="#f4f4ff" stroke="{INK}" stroke-width="1"/>')
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(13.6)} 20.4 C{X(11)} 21.4 {X(9.6)} 24.4 {X(9.8)} 27.2 L{X(12.6)} 27.4 C{X(12.6)} 25.2 {X(13.2)} 23.4 {X(14.4)} 22.4 Z", "url(#static-hood)"))
        p.append(f'<circle cx="{X(11.2)}" cy="28" r="1.3" fill="#ffd2b0" stroke="{INK}" stroke-width="0.9"/>')
    p.append(shape("M11.8 28.4 C11.4 24.4 12.4 20.6 15 19.4 H25 C27.6 20.6 28.6 24.4 28.2 28.4 Z", "url(#static-hood)"))
    p.append(shade("M24.6 19.8 C27.2 21.2 28 24.6 27.6 27.8 H23.6 C25.2 25.4 25.6 22.4 24.6 19.8 Z"))
    p.append(line("M15.4 24.6 H24.6 L23.6 27.6 H16.4 Z", "#4a2296", 0.6))
    p.append(line("M18.4 19.6 L18 23 M21.6 19.6 L22 23", "#ffffff", 0.5))
    # The hood, behind the TV.
    p.append(shape("M11.4 20.6 C9.6 18 10.2 14.4 12.6 13 H27.4 C29.8 14.4 30.4 18 28.6 20.6 Z", "url(#static-hood)"))
    for side in (1, -1):
        p.append(line(f"M20 4.2 L{20 + side * 5.2} 0.9", INK, 0.7))
        if on:
            p.append(glow(20 + side * 5.2, 0.9, 1.6, "g"))
        p.append(f'<circle cx="{20 + side * 5.2}" cy="0.9" r="0.7" fill="{lit("g", on)}" stroke="{INK}" stroke-width="0.5"/>')
    p.append(f'<rect x="8.6" y="4" width="22.8" height="15.6" rx="2.6" fill="url(#static-tv)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M9.4 17.4 H30.6 C30.6 18.6 30 19 28.8 19 H11.2 C10 19 9.4 18.6 9.4 17.4 Z"))
    p.append(highlight("M10.4 7.6 C10.6 6.4 11.2 5.8 12.2 5.6"))
    # The CRT screen: green phosphor face, static noise when idle.
    if on:
        p.append(glow(18, 11.6, 10, "g", ry=7.6, opacity=0.7))
    p.append(f'<rect x="10.4" y="5.8" width="15.4" height="11.8" rx="3" fill="{INK}"/>')
    p.append('<rect x="11.2" y="6.6" width="13.8" height="10.2" rx="2.4" fill="url(#screen)"/>')
    if s == "idle":
        p.append(line("M12.6 8.4 h1.4 M18.6 8 h2 M14.4 14.6 h1.6 M20.8 15.2 h1.4 M22.6 9.6 h1", "#8a90b8", 0.4, 0.6))
    if on:
        p.append(line("M11.8 9 H24.4 M11.8 12 H24.4 M11.8 15 H24.4", lit("g"), 0.3, 0.3))
    p.append(eyes(s, [(15.2, 10.6), (20.8, 10.6)], "g", 1.2))
    p.append(mouth(s, 18, 13.8, 2.4, lit("g", s != "idle")))
    p.append(line("M12.2 8 L13.6 7.4", "#ffffff", 0.4, 0.5))
    for cy in (8.6, 12):
        p.append(f'<circle cx="28.6" cy="{cy}" r="1.15" fill="url(#metal)" stroke="{INK}" stroke-width="0.6"/>')
    p.append(line("M27.4 15 H29.8 M27.4 16.4 H29.8", INK, 0.45))
    p.append(mark(s, 2, 4))
    return "".join(p)


def synth(s: str) -> str:
    """A teal android with big headphones, playing a keytar."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="synth-body" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#6ff5dc"/><stop offset="1" stop-color="#1a98aa"/></linearGradient></defs>'
    ]
    for cx in (16.6, 23.4):
        p.append(f'<rect x="{cx - 1}" y="27.4" width="2" height="2.6" fill="url(#metal)" stroke="{INK}" stroke-width="0.8"/>')
        p.append(f'<ellipse cx="{cx}" cy="30.5" rx="2.5" ry="1.1" fill="url(#synth-body)" stroke="{INK}" stroke-width="1"/>')
    p.append(shape("M14.4 19.4 H25.6 C26.6 19.4 27.2 20.2 27 21.2 L26 28 H14 L13 21.2 C12.8 20.2 13.4 19.4 14.4 19.4 Z", "url(#synth-body)"))
    p.append(shade("M24.4 20 H26 C26.6 20.4 26.6 21 26.4 21.8 L25.6 27.4 H23 C24.6 25 25 22.4 24.4 20 Z"))
    # The headphone band, the head and the cups.
    p.append(cable("M10.4 11.2 C9.6 2 30.4 2 29.6 11.2", "#2a2450", 1.2))
    p.append(f'<rect x="11.6" y="4.4" width="16.8" height="15.4" rx="6" fill="url(#synth-body)" stroke="{INK}" stroke-width="{SW}"/>')
    p.append(shade("M12.4 15.6 C15 18 25 18 27.6 15.6 C27.2 18 25.6 19.2 23 19.2 H17 C14.4 19.2 12.8 18 12.4 15.6 Z"))
    p.append(highlight("M13.8 8.2 C14.4 6.8 15.6 6 17.2 5.8"))
    p.append(f'<rect x="13.8" y="7.6" width="12.4" height="9" rx="3.6" fill="#f6f2ff" stroke="{INK}" stroke-width="0.7"/>')
    p.append(eyes(s, [(17.2, 11.2), (22.8, 11.2)], "m", 1.15))
    p.append(mouth(s, 20, 14.4, 2.2))
    for side in (1, -1):
        cx = 20 + side * 9.6
        if on:
            p.append(glow(cx, 12, 3.6, "m", ry=4.4))
        p.append(f'<rect x="{cx - 2.3}" y="8.2" width="4.6" height="7.6" rx="2.2" fill="#2a2450" stroke="{INK}" stroke-width="1"/>')
        p.append(line(f"M{cx + side * 1.1} 9.8 V14.2", lit("m", on), 0.8))
    # The keytar, tilted across the body.
    p.append('<g transform="rotate(-16 20 24.6)">')
    p.append(shape("M6.4 22.6 H27 L30 23.4 H35.6 V25.6 H30 L27 26.8 H8.4 C7 26.8 6 26 6 24.8 C6 23.6 6.4 22.6 6.4 22.6 Z", "#ff4f8a", 1))
    p.append('<path d="M8 26 H26.6 L27 26.8 H8.4 C7.8 26.8 7.4 26.6 7.2 26.2 Z" fill="#9a1f4a" opacity="0.5"/>')
    p.append(f'<rect x="9" y="23.4" width="14" height="2.4" rx="0.3" fill="#ffffff" stroke="{INK}" stroke-width="0.5"/>')
    p.append(line("".join(f"M{x} 23.4 V24.7 " for x in (10.8, 12.6, 16.2, 18, 19.8)), INK, 0.7))
    if on:
        p.append(f'<rect x="14.1" y="23.6" width="1.6" height="2" fill="{lit("c")}"/>')
        p.append(f'<rect x="19.4" y="23.6" width="1.6" height="2" fill="{lit("c")}"/>')
    for i, key in enumerate("cma"):
        p.append(f'<circle cx="{31.6 + i * 1.3}" cy="24.5" r="0.45" fill="{lit(key, on)}"/>')
    p.append("</g>")
    for cx, cy in ((10.6, 26.6), (29.4, 21.4)):
        p.append(f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="url(#synth-body)" stroke="{INK}" stroke-width="0.9"/>')
    if on:
        for x, y, key in ((32.4, 4.4, "m"), (35.6, 10, "c")):
            p.append(glow(x, y + 2, 2.4, key))
            p.append(line(f"M{x} {y + 3} V{y} L{x + 1.6} {y + 0.8}", lit(key), 0.6))
            p.append(f'<ellipse cx="{x - 0.6}" cy="{y + 3}" rx="0.8" ry="0.6" fill="{lit(key)}"/>')
    p.append(mark(s, 2, 2))
    return "".join(p)


def shard(s: str) -> str:
    """A small crystal data golem with a faceted body and glowing cracks."""
    on = s == "working"
    p = [
        '<defs><linearGradient id="shard-a" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#e2fdff"/><stop offset="1" stop-color="#5cc8ff"/></linearGradient>'
        '<linearGradient id="shard-b" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#9ed4ff"/><stop offset="1" stop-color="#3a5cd6"/></linearGradient></defs>'
    ]
    if on:
        p.append(glow(20, 17, 15, "c", ry=13, opacity=0.55))
    p.append(shape("M14.2 10.8 L12.8 3.6 L17.4 8.6 Z", "url(#shard-b)"))
    p.append(shape("M17.4 8 L20 0.8 L22.6 8 Z", "url(#shard-a)"))
    p.append(shape("M22.6 8.8 L27.4 4 L25.8 10.8 Z", "url(#shard-b)"))
    for side in (1, -1):
        def X(x: float) -> float:
            return 20 + side * (x - 20)
        p.append(shape(f"M{X(15.4)} 27 L{X(14.6)} 31.2 H{X(18.4)} L{X(18.6)} 27 Z", "url(#shard-b)"))
        p.append(shape(f"M{X(10.8)} 13.6 L{X(5.8)} 17 L{X(6.6)} 23.8 L{X(10.4)} 21.2 Z", "url(#shard-b)"))
    p.append(shape("M20 6.4 L28.6 10.6 L30.2 20.4 L25 27.8 H15 L9.8 20.4 L11.4 10.6 Z", "url(#shard-a)"))
    p.append(shade("M28.6 10.6 L30.2 20.4 L25 27.8 L24.2 21.8 L27 18.6 Z"))
    p.append(line("M9.8 20.4 L16 22 H24.2 L30.2 20.4 M16 22 L15 27.8 M24.2 22 L25 27.8", INK, 0.45, 0.5))
    p.append(highlight("M12.4 12 L19.4 8"))
    # The cracks glow with data when it works.
    cracks = "M12.6 12.8 L14.4 14.8 L13 17.4 M27 15.6 L25.6 18.4 L27.4 20.6 M19.2 22 L20.8 24.4 L19.6 27"
    if on:
        p.append(line(cracks, lit("m"), 1.8, 0.35))
    p.append(line(cracks, lit("m", on), 0.7))
    p.append(eyes(s, [(16.6, 14.6), (23.4, 14.6)], "v", 1.2))
    p.append(mouth(s, 20, 18.4, 2.4))
    p.append(mark(s, 2.5, 3))
    return "".join(p)


SPRITES = {
    "glitch": glitch,
    "proxy": proxy,
    "cipher": cipher,
    "vapor": vapor,
    "razor": razor,
    "chrome": chrome,
    "neon": neon,
    "static": static,
    "synth": synth,
    "shard": shard,
}
