"""Sprites batch A: aqua, blip, bling, bubbles, chrome, dialup, disco, fizz, flip, frosty."""

from .kit import LINE, Critter, gloss, line, orb, shine, spark

def _feet(color: str, *xs: float, y: float = 77) -> str:
    return "".join(f'<ellipse cx="{x}" cy="{y}" rx="7" ry="3" fill="{color}" {line(2)}/>' for x in xs)


CRITTERS: dict[str, Critter] = {
    "aqua": Critter(
        defs=gloss("aqua-body", "#c8f4ff", "#3cc8f4", "#1478c8"),
        body=(
            f'<path d="M50 6C58 20 76 34 76 52A26 26 0 0 1 24 52C24 34 42 20 50 6Z" fill="url(#aqua-body)" {LINE}/>'
            + shine(42, 30, 9, 13)
            + spark(64, 62, 3)
            + f'<ellipse cx="40" cy="77" rx="7" ry="3" fill="#ff8ac2" {line(2)}/>'
            + f'<ellipse cx="60" cy="77" rx="7" ry="3" fill="#ff8ac2" {line(2)}/>'
        ),
        eyes=[(42, 50), (58, 50)],
        mouth=(50, 60),
        lit='<circle cx="50" cy="12" r="4" fill="#ffd23a" opacity=".9"/>',
    ),
    "blip": Critter(
        defs=gloss("blip-body", "#efe6ff", "#a98cf0", "#6a4cc0") + gloss("blip-screen", "#ffffff", "#e6fff4", "#bdf0dc"),
        body=(
            f'<path d="M42 24L32 8M58 24L68 8" fill="none" {line(3)}/>'
            + f'<circle cx="32" cy="8" r="4" fill="#ff8ac2" {line(2)}/>'
            + f'<circle cx="68" cy="8" r="4" fill="#ff8ac2" {line(2)}/>'
            + f'<rect x="24" y="22" width="52" height="50" rx="16" fill="url(#blip-body)" {LINE}/>'
            + f'<rect x="30" y="30" width="40" height="34" rx="11" fill="url(#blip-screen)" {line(2)}/>'
            + shine(40, 27, 12, 4)
            + f'<ellipse cx="38" cy="77" rx="7" ry="3" fill="#ff8ac2" {line(2)}/>'
            + f'<ellipse cx="62" cy="77" rx="7" ry="3" fill="#ff8ac2" {line(2)}/>'
        ),
        eyes=[(42, 44), (58, 44)],
        mouth=(50, 55),
        lit=(
            '<circle cx="32" cy="8" r="4" fill="#ffd23a" opacity=".9"/><circle cx="68" cy="8" r="4" fill="#ffd23a" opacity=".9"/>'
            '<rect x="30" y="30" width="40" height="34" rx="11" fill="#7cf0ff" opacity=".35"/>'
        ),
    ),
    "bling": Critter(
        defs=gloss("bling-body", "#ffd8ec", "#ff6fb5", "#c42a82"),
        body=(
            f'<path d="M34 14L66 14L78 32L50 74L22 32Z" fill="url(#bling-body)" {LINE}/>'
            + f'<path d="M22 32L78 32M34 14L42 32M66 14L58 32M42 32L50 14L58 32" fill="none" stroke="#ffffff" stroke-width="1.6" '
            'stroke-linejoin="round" opacity=".8"/>'
            + '<path d="M36 18L44 18L38 30Z" fill="#ffffff" opacity=".7"/>'
            + spark(70, 52, 4)
            + _feet("#ffd23a", 50, y=77)
        ),
        eyes=[(42, 43), (58, 43)],
        mouth=(50, 54),
        lit=spark(50, 6, 6, "#ffd23a") + spark(30, 22, 4, "#ffd23a"),
    ),
    "bubbles": Critter(
        defs=orb("bubbles-body", "#fbf6ff", "#b48cf0"),
        body=(
            f'<path d="M50 14C68 10 80 28 78 46C77 62 66 72 50 72C32 72 22 62 22 46C22 28 32 18 50 14Z" '
            f'fill="url(#bubbles-body)" {LINE}/>'
            + f'<circle cx="74" cy="20" r="5" fill="url(#bubbles-body)" {line(2)}/>'
            + f'<circle cx="26" cy="68" r="4" fill="url(#bubbles-body)" opacity=".9" {line(2)}/>'
            + shine(38, 26, 12, 7)
            + f'<ellipse cx="40" cy="77" rx="6" ry="3" fill="#8ad8ff" {line(2)}/>'
            + f'<ellipse cx="60" cy="77" rx="6" ry="3" fill="#8ad8ff" {line(2)}/>'
        ),
        eyes=[(41, 46), (59, 46)],
        mouth=(50, 57),
        lit='<circle cx="50" cy="44" r="27" fill="#ffffff" opacity=".25"/><circle cx="74" cy="20" r="3" fill="#ffd23a"/>',
    ),
    "chrome": Critter(
        defs=gloss("chrome-body", "#ffffff", "#b8c4d4", "#5e6e8a") + gloss("chrome-visor", "#ffffff", "#eef6ff", "#cfe0f4"),
        body=(
            f'<path d="M50 22V10" fill="none" {line(3)}/>'
            + f'<circle cx="50" cy="8" r="4.5" fill="#ff8ac2" {line(2)}/>'
            + f'<path d="M22 64A28 42 0 0 1 78 64Z" fill="url(#chrome-body)" {LINE}/>'
            + f'<rect x="20" y="62" width="60" height="12" rx="6" fill="url(#chrome-body)" {LINE}/>'
            + f'<ellipse cx="50" cy="48" rx="21" ry="13" fill="url(#chrome-visor)" {line(2)}/>'
            + shine(40, 30, 10, 6)
            + _feet("#3cc8f4", 36, 64)
        ),
        eyes=[(42, 47), (58, 47)],
        mouth=(50, 57),
        lit='<circle cx="50" cy="8" r="4.5" fill="#ffd23a" opacity=".95"/><circle cx="30" cy="68" r="2" fill="#ffd23a"/>',
    ),
    "dialup": Critter(
        defs=gloss("dialup-body", "#d8fff4", "#5ed0c0", "#228a92") + gloss("dialup-screen", "#ffffff", "#f0ffff", "#d0f4f4"),
        body=(
            f'<path d="M66 36L74 12" fill="none" {line(3)}/>'
            + f'<circle cx="74" cy="11" r="4" fill="#ff8ac2" {line(2)}/>'
            + f'<rect x="22" y="32" width="56" height="42" rx="10" fill="url(#dialup-body)" {LINE}/>'
            + f'<rect x="29" y="37" width="42" height="23" rx="8" fill="url(#dialup-screen)" {line(2)}/>'
            + shine(38, 36, 12, 3)
            + f'<circle cx="32" cy="67" r="2.6" fill="#c8e8e8" {line(1.6)}/>'
            + f'<circle cx="42" cy="67" r="2.6" fill="#c8e8e8" {line(1.6)}/>'
            + f'<circle cx="52" cy="67" r="2.6" fill="#c8e8e8" {line(1.6)}/>'
            + f'<path d="M62 67H70" fill="none" {line(2.4)}/>'
            + _feet("#ff8ac2", 34, 66)
        ),
        eyes=[(42, 46), (58, 46)],
        mouth=(50, 55),
        lit=(
            '<circle cx="74" cy="11" r="4" fill="#ffd23a" opacity=".95"/>'
            '<circle cx="32" cy="67" r="2.6" fill="#ffd23a"/><circle cx="42" cy="67" r="2.6" fill="#7cf06a"/>'
            '<circle cx="52" cy="67" r="2.6" fill="#ffd23a"/>'
        ),
    ),
    "disco": Critter(
        defs=(
            orb("disco-body", "#ffffff", "#8a9cc0")
            + '<clipPath id="disco-clip"><circle cx="50" cy="46" r="28"/></clipPath>'
        ),
        body=(
            f'<path d="M50 4V16" fill="none" {line(2.4)}/>'
            + f'<rect x="44" y="14" width="12" height="7" rx="2" fill="#ffd23a" {line(2)}/>'
            + f'<circle cx="50" cy="46" r="28" fill="url(#disco-body)" {LINE}/>'
            + '<g clip-path="url(#disco-clip)" fill="none" stroke="#0b2545" stroke-width="1" opacity=".35">'
            '<path d="M22 28H78M22 37H78M22 56H78M22 65H78M30 18V74M40 18V74M60 18V74M70 18V74"/></g>'
            + '<ellipse cx="50" cy="51" rx="19" ry="12" fill="#f4f8ff" opacity=".95"/>'
            + '<path d="M30 30L36 24L40 30ZM62 28L68 34L60 36ZM28 58L34 66L26 64Z" fill="#8ad8ff" opacity=".8"/>'
            + shine(38, 30, 9, 6)
            + _feet("#ff8ac2", 38, 62)
        ),
        eyes=[(42, 47), (58, 47)],
        mouth=(50, 57),
        lit=spark(34, 36, 4, "#ffd23a") + spark(68, 60, 4, "#ffd23a"),
    ),
    "fizz": Critter(
        defs=gloss("fizz-body", "#e8ffb8", "#8ae02c", "#3c9a14"),
        body=(
            f'<rect x="28" y="18" width="44" height="54" rx="9" fill="url(#fizz-body)" {LINE}/>'
            + f'<ellipse cx="50" cy="18" rx="22" ry="5" fill="#dfe8f4" {line(2.4)}/>'
            + f'<ellipse cx="50" cy="18" rx="9" ry="2" fill="#8896b0" {line(1.6)}/>'
            + '<rect x="33" y="31" width="34" height="32" rx="9" fill="#f6ffe0"/>'
            + shine(38, 25, 5, 4)
            + f'<circle cx="74" cy="22" r="4" fill="#e8ffd8" {line(2)}/>'
            + f'<circle cx="68" cy="8" r="3" fill="#e8ffd8" {line(2)}/>'
            + f'<circle cx="80" cy="10" r="2.2" fill="#e8ffd8" {line(1.6)}/>'
            + _feet("#ff8ac2", 38, 62)
        ),
        eyes=[(43, 43), (57, 43)],
        mouth=(50, 54),
        lit=(
            '<circle cx="74" cy="22" r="3" fill="#ffd23a"/><circle cx="68" cy="8" r="2" fill="#ffd23a"/>'
            + spark(50, 4, 3, "#ffd23a")
        ),
    ),
    "flip": Critter(
        defs=gloss("flip-body", "#ffe0f0", "#ff7cba", "#c8387e") + gloss("flip-screen", "#ffffff", "#ecffff", "#c8f0f4"),
        body=(
            f'<path d="M62 14V4" fill="none" {line(3)}/>'
            + f'<circle cx="62" cy="4" r="3" fill="#3cc8f4" {line(2)}/>'
            + f'<rect x="28" y="12" width="44" height="38" rx="10" fill="url(#flip-body)" {LINE}/>'
            + f'<rect x="33" y="17" width="34" height="28" rx="7" fill="url(#flip-screen)" {line(2)}/>'
            + f'<rect x="31" y="50" width="38" height="6" rx="3" fill="#c8387e" {line(2)}/>'
            + f'<rect x="28" y="54" width="44" height="22" rx="9" fill="url(#flip-body)" {LINE}/>'
            + '<circle cx="42" cy="62" r="1.8" fill="#ffffff"/><circle cx="50" cy="62" r="1.8" fill="#ffffff"/>'
            '<circle cx="58" cy="62" r="1.8" fill="#ffffff"/><circle cx="42" cy="69" r="1.8" fill="#ffffff"/>'
            '<circle cx="50" cy="69" r="1.8" fill="#ffffff"/><circle cx="58" cy="69" r="1.8" fill="#ffffff"/>'
            + shine(40, 16, 9, 3)
        ),
        eyes=[(43, 29), (57, 29)],
        mouth=(50, 39),
        lit='<circle cx="62" cy="4" r="3" fill="#ffd23a"/><rect x="33" y="17" width="34" height="28" rx="7" fill="#7cf0ff" opacity=".3"/>',
    ),
    "frosty": Critter(
        defs=gloss("frosty-body", "#f4fcff", "#b4e4fa", "#74b8ea"),
        body=(
            f'<rect x="24" y="18" width="52" height="56" rx="14" fill="url(#frosty-body)" {LINE}/>'
            + '<path d="M30 30L36 24M64 68L70 62M70 30L66 36" fill="none" stroke="#ffffff" stroke-width="2" '
            'stroke-linecap="round" opacity=".9"/>'
            + shine(40, 28, 12, 6)
            + spark(68, 26, 4)
            + spark(32, 66, 3)
            + _feet("#b4e4fa", 38, 62)
        ),
        eyes=[(42, 44), (58, 44)],
        mouth=(50, 55),
        lit='<rect x="24" y="18" width="52" height="56" rx="14" fill="#ffffff" opacity=".3"/>' + spark(50, 10, 4, "#ffd23a"),
    ),
}
