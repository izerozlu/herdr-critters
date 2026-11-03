"""Sprites batch B: glossy, gummy, jelly, kazoo, laser, lime, mixtape, modem, nano, orbit."""

from .kit import LINE, Critter, gloss, line, orb, shine, spark

CRITTERS: dict[str, Critter] = {
    "glossy": Critter(
        defs=gloss("glossy-body", "#d8f8ff", "#5ad4f8", "#1a86d0"),
        body=(
            f'<ellipse cx="50" cy="51" rx="29" ry="27" fill="url(#glossy-body)" {LINE}/>'
            + '<ellipse cx="50" cy="51" rx="24" ry="22" fill="none" stroke="#ffffff" stroke-width="1.6" opacity=".55"/>'
            + shine(42, 33, 16, 10)
            + spark(68, 66, 3)
        ),
        eyes=[(42, 50), (58, 50)],
        mouth=(50, 60),
        lit='<ellipse cx="50" cy="70" rx="14" ry="3.5" fill="#ffd23a" opacity=".85"/>',
    ),
    "gummy": Critter(
        defs=gloss("gummy-body", "#ffc8dc", "#ff5a8a", "#d02870"),
        body=(
            f'<circle cx="35" cy="19" r="7" fill="url(#gummy-body)" {LINE}/>'
            + f'<circle cx="65" cy="19" r="7" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="29" cy="58" rx="6" ry="8" transform="rotate(25 29 58)" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="71" cy="58" rx="6" ry="8" transform="rotate(-25 71 58)" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="50" cy="62" rx="20" ry="15" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="38" cy="73" rx="8" ry="5.5" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="62" cy="73" rx="8" ry="5.5" fill="url(#gummy-body)" {LINE}/>'
            + f'<ellipse cx="50" cy="36" rx="21" ry="18" fill="url(#gummy-body)" {LINE}/>'
            + '<ellipse cx="50" cy="42" rx="9" ry="6" fill="#ffd9e6" opacity=".9"/>'
            + shine(41, 26, 9, 6)
            + shine(44, 56, 8, 5)
        ),
        eyes=[(42, 33), (58, 33)],
        mouth=(50, 43),
        eye=3.2,
        lit='<ellipse cx="50" cy="64" rx="9" ry="6" fill="#ffd23a" opacity=".6"/>',
    ),
    "jelly": Critter(
        defs=gloss("jelly-body", "#f4dcff", "#d8a0ff", "#9040d0"),
        body=(
            "".join(
                f'<path d="M{x} 44Q{x - 5} 56 {x} 64T{x} 78" fill="none" stroke="{"#0b2545"}" stroke-width="7" '
                'stroke-linecap="round"/>'
                f'<path d="M{x} 44Q{x - 5} 56 {x} 64T{x} 78" fill="none" stroke="#e8b8ff" stroke-width="3" '
                'stroke-linecap="round"/>'
                for x in (35, 46, 57, 67)
            )
            + '<path d="M22 46A28 32 0 0 1 78 46Q73 51 67 46Q58 52 50 46Q42 52 33 46Q27 51 22 46Z" '
            f'fill="url(#jelly-body)" {LINE}/>'
            + shine(41, 20, 12, 9)
            + spark(68, 24, 3)
        ),
        eyes=[(42, 32), (58, 32)],
        mouth=(50, 42),
        lit='<circle cx="50" cy="14" r="4" fill="#ffd23a" opacity=".9"/>',
    ),
    "kazoo": Critter(
        defs=gloss("kazoo-body", "#fff6b8", "#ffd23a", "#e8921a") + gloss("kazoo-hat", "#e8c8ff", "#a86ae8", "#6a30b8"),
        body=(
            f'<ellipse cx="42" cy="77" rx="6" ry="3" fill="#ff9a3a" {line(2)}/>'
            + f'<ellipse cx="58" cy="77" rx="6" ry="3" fill="#ff9a3a" {line(2)}/>'
            + f'<circle cx="50" cy="51" r="26" fill="url(#kazoo-body)" {LINE}/>'
            + f'<path d="M26 56Q20 64 30 68Q32 62 30 58Z" fill="url(#kazoo-body)" {line(2)}/>'
            + f'<path d="M61 55H77" stroke="{"#0b2545"}" stroke-width="9" stroke-linecap="round"/>'
            + '<path d="M61 55H77" stroke="#ff9a3a" stroke-width="5" stroke-linecap="round"/>'
            + f'<ellipse cx="80" cy="55" rx="3.5" ry="6" fill="#ffd23a" {line(2)}/>'
            + f'<path d="M50 6L38 28Q50 32 62 28Z" fill="url(#kazoo-hat)" {LINE}/>'
            + '<path d="M44 18L56 18M41 24L59 24" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity=".8"/>'
            + f'<circle cx="50" cy="6" r="3.5" fill="#ff5a8a" {line(2)}/>'
            + shine(40, 42, 8, 7)
        ),
        eyes=[(41, 46), (59, 46)],
        mouth=(50, 57),
        lit='<ellipse cx="80" cy="55" rx="3.5" ry="6" fill="#fff6c0"/>' + spark(72, 44, 4, "#ffd23a"),
    ),
    "laser": Critter(
        defs=gloss("laser-body", "#f6faff", "#b8c8dc", "#6f86a6") + gloss("laser-visor", "#e8fcff", "#a0e8ff", "#5ac0f0"),
        body=(
            f'<path d="M50 24V11" stroke="#0b2545" stroke-width="3" stroke-linecap="round"/>'
            + f'<circle cx="50" cy="9" r="4.5" fill="#ff5a8a" {line(2)}/>'
            + f'<ellipse cx="38" cy="77" rx="8" ry="3" fill="#6f86a6" {line(2)}/>'
            + f'<ellipse cx="62" cy="77" rx="8" ry="3" fill="#6f86a6" {line(2)}/>'
            + f'<circle cx="23" cy="48" r="4.5" fill="#b8c8dc" {line(2)}/>'
            + f'<circle cx="77" cy="48" r="4.5" fill="#b8c8dc" {line(2)}/>'
            + f'<rect x="26" y="24" width="48" height="53" rx="14" fill="url(#laser-body)" {LINE}/>'
            + f'<rect x="32" y="33" width="36" height="28" rx="10" fill="url(#laser-visor)" {LINE}/>'
            + '<path d="M38 69H62" stroke="#6f86a6" stroke-width="2.4" stroke-linecap="round"/>'
            + shine(40, 28, 10, 4)
        ),
        eyes=[(42.5, 44), (57.5, 44)],
        mouth=(50, 54),
        eye=3.2,
        lit=(
            f'<circle cx="50" cy="9" r="4.5" fill="#ffd23a" {line(2)}/>'
            + spark(50, 9, 9, "#ffd23a")
            + '<circle cx="42" cy="69" r="1.6" fill="#ffd23a"/><circle cx="58" cy="69" r="1.6" fill="#ffd23a"/>'
        ),
    ),
    "lime": Critter(
        defs=gloss("lime-body", "#eeffb0", "#9ae64a", "#3a9a1a") + gloss("lime-leaf", "#c8ff80", "#5cc828", "#2a8a18"),
        body=(
            f'<circle cx="50" cy="50" r="28" fill="url(#lime-body)" {LINE}/>'
            + '<path d="M50 24V30M33 31L36 34M67 31L64 34" stroke="#ffffff" stroke-width="2" stroke-linecap="round" opacity=".5"/>'
            + f'<path d="M50 23Q52 12 66 10Q78 10 77 14Q74 26 60 26Q54 26 50 23Z" fill="url(#lime-leaf)" {LINE}/>'
            + '<path d="M54 22Q62 16 72 13" fill="none" stroke="#2a8a18" stroke-width="1.6" stroke-linecap="round"/>'
            + shine(38, 38, 10, 8)
            + spark(68, 66, 3)
        ),
        eyes=[(42, 50), (58, 50)],
        mouth=(50, 60),
        lit='<ellipse cx="50" cy="70" rx="12" ry="3.5" fill="#ffd23a" opacity=".85"/>',
    ),
    "mixtape": Critter(
        defs=gloss("mixtape-body", "#e8ccff", "#a86ae8", "#6a30b8") + gloss("mixtape-low", "#f4f8ff", "#c8d4e8", "#8aa0c0"),
        body=(
            f'<rect x="22" y="24" width="56" height="52" rx="8" fill="url(#mixtape-body)" {LINE}/>'
            + f'<rect x="28" y="29" width="44" height="25" rx="4" fill="#fffbe8" {line(2)}/>'
            + '<path d="M29 34H71" stroke="#ff5a8a" stroke-width="2.4"/>'
            + f'<path d="M30 76L35 60H65L70 76Z" fill="url(#mixtape-low)" {line(2.4)}/>'
            + f'<circle cx="40" cy="64" r="5" fill="#ffffff" {line(2)}/>'
            + f'<circle cx="60" cy="64" r="5" fill="#ffffff" {line(2)}/>'
            + '<circle cx="40" cy="64" r="1.8" fill="#0b2545"/><circle cx="60" cy="64" r="1.8" fill="#0b2545"/>'
            + shine(36, 27, 10, 3)
        ),
        eyes=[(42, 41), (58, 41)],
        mouth=(50, 50),
        eye=3.2,
        lit='<circle cx="40" cy="64" r="2.4" fill="#ffd23a"/><circle cx="60" cy="64" r="2.4" fill="#ffd23a"/>',
    ),
    "modem": Critter(
        defs=gloss("modem-body", "#c0e4ff", "#4a9cf0", "#1c52b8"),
        body=(
            f'<path d="M38 24L30 7M62 24L70 7" stroke="#0b2545" stroke-width="3" stroke-linecap="round"/>'
            + f'<circle cx="30" cy="7" r="3.5" fill="#ffffff" {line(2)}/>'
            + f'<circle cx="70" cy="7" r="3.5" fill="#ffffff" {line(2)}/>'
            + f'<rect x="26" y="22" width="48" height="56" rx="18" fill="url(#modem-body)" {LINE}/>'
            + f'<rect x="32" y="29" width="36" height="28" rx="11" fill="#e8f6ff" {line(2)}/>'
            + "".join(f'<circle cx="{x}" cy="67" r="2.6" fill="#7ab0e8" {line(1.6)}/>' for x in (38, 46, 54, 62))
            + shine(38, 25, 9, 3)
        ),
        eyes=[(42.5, 40), (57.5, 40)],
        mouth=(50, 50),
        eye=3.2,
        lit=(
            "".join(f'<circle cx="{x}" cy="67" r="2.6" fill="#ffd23a" {line(1.6)}/>' for x in (38, 54))
            + "".join(f'<circle cx="{x}" cy="67" r="2.6" fill="#7dff6a" {line(1.6)}/>' for x in (46, 62))
            + '<circle cx="30" cy="7" r="3.5" fill="#ffd23a"/><circle cx="70" cy="7" r="3.5" fill="#ffd23a"/>'
        ),
    ),
    "nano": Critter(
        defs=gloss("nano-body", "#ffffff", "#c8d4e8", "#7e94b8") + orb("nano-wheel", "#ffffff", "#aab8d0"),
        body=(
            f'<rect x="32" y="4" width="36" height="74" rx="11" fill="url(#nano-body)" {LINE}/>'
            + f'<rect x="37" y="9" width="26" height="33" rx="5" fill="#e8fbff" {line(2)}/>'
            + f'<circle cx="50" cy="60" r="14" fill="url(#nano-wheel)" {line(2.4)}/>'
            + f'<circle cx="50" cy="60" r="5.5" fill="#7ad8f8" {line(2)}/>'
            + shine(43, 10, 7, 3)
        ),
        eyes=[(43, 22), (57, 22)],
        mouth=(50, 33),
        eye=3,
        lit='<rect x="38" y="10" width="24" height="31" rx="4" fill="#ffd23a" opacity=".4"/>',
    ),
    "orbit": Critter(
        defs=orb("orbit-body", "#fff0c0", "#e8721a"),
        body=(
            '<g transform="rotate(-12 50 62)">'
            '<path d="M18 62A32 8 0 0 1 82 62" fill="none" stroke="#0b2545" stroke-width="9" stroke-linecap="round"/>'
            '<path d="M18 62A32 8 0 0 1 82 62" fill="none" stroke="#ff8ac2" stroke-width="4.4" stroke-linecap="round"/></g>'
            + f'<circle cx="50" cy="48" r="26" fill="url(#orbit-body)" {LINE}/>'
            + '<g transform="rotate(-12 50 62)">'
            '<path d="M18 62A32 8 0 0 0 82 62" fill="none" stroke="#0b2545" stroke-width="9" stroke-linecap="round"/>'
            '<path d="M18 62A32 8 0 0 0 82 62" fill="none" stroke="#ff8ac2" stroke-width="4.4" stroke-linecap="round"/></g>'
            + shine(40, 33, 10, 7)
            + spark(78, 22, 3)
        ),
        eyes=[(42, 44), (58, 44)],
        mouth=(50, 54),
        lit=spark(24, 22, 5, "#ffd23a") + spark(70, 74, 4, "#ffd23a"),
    ),
}
