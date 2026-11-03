"""Sprites batch C: pager, plasma, qwerty, skater, techno, tunes, vapor, wifi, xtreme, yoyo."""

from .kit import INK, LINE, Critter, gloss, line, orb, shine, spark

CRITTERS: dict[str, Critter] = {
    "pager": Critter(
        defs=gloss("pager-body", "#f4f8ff", "#b8c8e0", "#6f86ad") + gloss("pager-screen", "#d8ff9a", "#a6e83a", "#6cb81c"),
        body=(
            f'<rect x="25" y="12" width="50" height="66" rx="13" fill="url(#pager-body)" {LINE}/>'
            + f'<rect x="32" y="19" width="36" height="17" rx="5" fill="url(#pager-screen)" {line(2)}/>'
            + f'<path d="M36 25H50M36 30H60" {line(2)}/>'
            + shine(42, 24, 14, 6)
            + f'<circle cx="38" cy="72" r="2" fill="#ff8ac2" {line(1.5)}/>'
            + f'<circle cx="50" cy="72" r="2" fill="#ff8ac2" {line(1.5)}/>'
            + f'<circle cx="62" cy="72" r="2" fill="#ff8ac2" {line(1.5)}/>'
        ),
        eyes=[(42, 49), (58, 49)],
        mouth=(50, 59),
        lit=f'<rect x="32" y="19" width="36" height="17" rx="5" fill="#ffd23a" opacity=".85" {line(2)}/>'
        f'<path d="M36 25H50M36 30H60" {line(2)}/>',
    ),
    "plasma": Critter(
        defs=orb("plasma-ball", "#ffe0ff", "#a24cdc") + gloss("plasma-base", "#e6ecf8", "#9fb0cc", "#5a6f98"),
        body=(
            f'<path d="M34 78L38 62H62L66 78Z" fill="url(#plasma-base)" {LINE}/>'
            + f'<circle cx="50" cy="38" r="28" fill="url(#plasma-ball)" {LINE}/>'
            + shine(40, 20, 12, 8)
            + f'<path d="M50 62L44 52L36 56M50 62L58 52L66 54" fill="none" stroke="#ff8ac2" stroke-width="2" stroke-linecap="round"/>'
        ),
        eyes=[(42, 38), (58, 38)],
        mouth=(50, 48),
        lit=f'<path d="M26 54L36 50L30 44M74 54L64 50L70 44" fill="none" stroke="#ffd23a" stroke-width="3" '
        'stroke-linejoin="round" stroke-linecap="round"/>',
    ),
    "qwerty": Critter(
        defs=gloss("qwerty-side", "#6fe0ff", "#2aa4e0", "#1664b0") + gloss("qwerty-top", "#f4fdff", "#bff0ff", "#7cd0f0"),
        body=(
            f'<rect x="20" y="22" width="60" height="56" rx="13" fill="url(#qwerty-side)" {LINE}/>'
            + f'<rect x="27" y="12" width="46" height="46" rx="10" fill="url(#qwerty-top)" {LINE}/>'
            + shine(42, 20, 14, 7)
            + spark(66, 50, 3, "#3cc8f4")
        ),
        eyes=[(42, 34), (58, 34)],
        mouth=(50, 45),
        lit=f'<rect x="27" y="12" width="46" height="46" rx="10" fill="#ffd23a" opacity=".35"/>'
        f'<rect x="21.5" y="68" width="57" height="8" rx="4" fill="#ffd23a" opacity=".8"/>',
    ),
    "skater": Critter(
        defs=gloss("skater-body", "#d8ffa0", "#8fe03a", "#4ea81c") + gloss("skater-deck", "#ff9ac8", "#ff4fa0", "#c42878"),
        body=(
            f'<path d="M26 72Q50 24 74 72Z" fill="url(#skater-body)" {LINE}/>'.replace("Q50 24", "C26 20 74 20")
            + shine(38, 46, 6, 6)
            + f'<rect x="16" y="68" width="68" height="7" rx="3.5" fill="url(#skater-deck)" {LINE}/>'
            + f'<circle cx="30" cy="76" r="3.6" fill="#e6ecf8" {line(2)}/>'
            + f'<circle cx="70" cy="76" r="3.6" fill="#e6ecf8" {line(2)}/>'
        ),
        eyes=[(43, 50), (57, 50)],
        mouth=(50, 60),
        lit='<path d="M8 66H15M6 72H14" stroke="#3cc8f4" stroke-width="2.4" stroke-linecap="round"/>'
        '<circle cx="30" cy="76" r="1.6" fill="#ffd23a"/><circle cx="70" cy="76" r="1.6" fill="#ffd23a"/>',
    ),
    "techno": Critter(
        defs=gloss("techno-body", "#f4f8ff", "#b8c8e0", "#6f86ad") + gloss("techno-phones", "#ffa0d0", "#ff4fa0", "#c42878"),
        body=(
            f'<path d="M50 26V12" {LINE}/><circle cx="50" cy="10" r="4" fill="#ff8ac2" {line(2)}/>'
            + f'<rect x="38" y="68" width="10" height="10" rx="4" fill="#9fb0cc" {line(2)}/>'
            + f'<rect x="52" y="68" width="10" height="10" rx="4" fill="#9fb0cc" {line(2)}/>'
            + f'<rect x="29" y="24" width="42" height="48" rx="14" fill="url(#techno-body)" {LINE}/>'
            + shine(42, 32, 10, 5)
            + f'<path d="M27 46A23 23 0 0 1 73 46" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            + '<path d="M27 46A23 23 0 0 1 73 46" fill="none" stroke="#ff4fa0" stroke-width="3.6" stroke-linecap="round"/>'
            + f'<rect x="19" y="36" width="12" height="24" rx="6" fill="url(#techno-phones)" {LINE}/>'
            + f'<rect x="69" y="36" width="12" height="24" rx="6" fill="url(#techno-phones)" {LINE}/>'
        ),
        eyes=[(42, 44), (58, 44)],
        mouth=(50, 55),
        lit='<circle cx="50" cy="10" r="4" fill="#ffd23a"/>'
        '<path d="M12 40Q9 48 12 56M88 40Q91 48 88 56" fill="none" stroke="#3cc8f4" stroke-width="2.4" stroke-linecap="round"/>',
    ),
    "tunes": Critter(
        defs=orb("tunes-head", "#e6c8ff", "#8a4fd8") + gloss("tunes-stem", "#d8b8ff", "#a070e8", "#6a3cb8"),
        body=(
            f'<path d="M64 14H71V60H64Z" fill="url(#tunes-stem)" {LINE}/>'
            + f'<path d="M71 14C71 28 82 28 80 42C76 36 73 34 71 34Z" fill="url(#tunes-stem)" {LINE}/>'.replace("82 28 80 42", "79 26 78 40")
            + f'<ellipse cx="46" cy="58" rx="25" ry="20" fill="url(#tunes-head)" {LINE}/>'
            + shine(36, 46, 11, 7)
        ),
        eyes=[(39, 56), (53, 56)],
        mouth=(46, 66),
        lit='<path d="M74 22L82 20M74 28L83 28" stroke="#ffd23a" stroke-width="2.4" stroke-linecap="round"/>',
    ),
    "vapor": Critter(
        defs=gloss("vapor-body", "#f0e0ff", "#c89cff", "#8a5cd8"),
        body=(
            f'<path d="M26 70C16 68 16 52 28 50C26 36 42 28 52 34C60 24 78 32 74 48C84 52 82 68 74 70'
            f'C72 80 62 80 58 74C54 80 46 80 42 74C38 80 28 80 26 70Z" fill="url(#vapor-body)" {LINE}/>'
            + shine(40, 40, 11, 7)
            + spark(68, 42, 3)
        ),
        eyes=[(42, 54), (58, 54)],
        mouth=(50, 64),
        lit='<ellipse cx="50" cy="52" rx="26" ry="16" fill="#ffd23a" opacity=".2"/>',
    ),
    "wifi": Critter(
        defs=gloss("wifi-body", "#d8f6ff", "#5cd0f8", "#1c84d0"),
        body=(
            f'<path d="M24 78C24 54 34 44 50 44C66 44 76 54 76 78Z" fill="url(#wifi-body)" {LINE}/>'
            + shine(40, 54, 9, 6)
            + "".join(
                f'<path d="M{50 - r * 0.707:.1f} {38 - r * 0.707:.1f}A{r} {r} 0 0 1 {50 + r * 0.707:.1f} {38 - r * 0.707:.1f}" '
                f'fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
                f'<path d="M{50 - r * 0.707:.1f} {38 - r * 0.707:.1f}A{r} {r} 0 0 1 {50 + r * 0.707:.1f} {38 - r * 0.707:.1f}" '
                'fill="none" stroke="#c8ff5a" stroke-width="3.4" stroke-linecap="round"/>'
                for r in (10, 20, 30)
            )
        ),
        eyes=[(42, 60), (58, 60)],
        mouth=(50, 70),
        lit="".join(
            f'<path d="M{50 - r * 0.707:.1f} {38 - r * 0.707:.1f}A{r} {r} 0 0 1 {50 + r * 0.707:.1f} {38 - r * 0.707:.1f}" '
            'fill="none" stroke="#ffd23a" stroke-width="3.4" stroke-linecap="round"/>'
            for r in (10, 20, 30)
        ),
    ),
    "xtreme": Critter(
        defs=gloss("xtreme-body", "#ffe8b0", "#ffb84a", "#e07a1c")
        + gloss("xtreme-hair", "#ffffff", "#8fdcff", "#2a8ae8")
        + gloss("xtreme-shades", "#6a8ac8", "#1b3a6b", "#0b1d3a"),
        body=(
            f'<ellipse cx="50" cy="57" rx="26" ry="21" fill="url(#xtreme-body)" {LINE}/>'
            + shine(40, 52, 10, 6)
            + f'<path d="M30 42L27 24L37 32L39 10L47 28L52 5L58 28L65 10L65 32L74 24L70 42Z" fill="url(#xtreme-hair)" {LINE}/>'
            + f'<path d="M28 34Q50 28 72 34L70 43Q61 46 54 41H46Q39 46 30 43Z" fill="url(#xtreme-shades)" {LINE}/>'
            + '<path d="M33 36Q40 34 46 36" fill="none" stroke="#9fe8ff" stroke-width="2" stroke-linecap="round"/>'
            + '<path d="M56 36Q62 34 67 36" fill="none" stroke="#9fe8ff" stroke-width="2" stroke-linecap="round"/>'
        ),
        eyes=[(42, 58), (58, 58)],
        mouth=(50, 68),
        lit='<circle cx="52" cy="5" r="3.5" fill="#ffd23a"/><circle cx="39" cy="10" r="3" fill="#ffd23a"/>'
        '<circle cx="65" cy="10" r="3" fill="#ffd23a"/>',
    ),
    "yoyo": Critter(
        defs=gloss("yoyo-ring", "#ffb0d8", "#ff4fa0", "#b82070") + orb("yoyo-face", "#ffffff", "#ffd8ee"),
        body=(
            f'<path d="M50 26V18" {LINE}/><ellipse cx="50" cy="12" rx="9" ry="6" fill="none" {LINE}/>'
            + f'<circle cx="50" cy="52" r="26" fill="url(#yoyo-ring)" {LINE}/>'
            + f'<circle cx="50" cy="52" r="18" fill="url(#yoyo-face)" {line(2)}/>'
            + shine(40, 34, 12, 5)
        ),
        eyes=[(43, 50), (57, 50)],
        mouth=(50, 60),
        lit='<circle cx="50" cy="52" r="18" fill="#ffd23a" opacity=".3"/><ellipse cx="50" cy="12" rx="9" ry="6" fill="none" stroke="#ffd23a" stroke-width="1.6"/>',
    ),
}
