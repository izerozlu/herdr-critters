"""Batch B: bugsy the rat, louie the pigeon, slick the raccoon."""

import skia

from .kit import BLOOD, INK, Critter, color, cut, oval, paint, poly, stroked, svgpath, union

# ---- bugsy: a skinny rat informant in a flat cap and a striped shirt -------------------

_bugsy_torso = svgpath("M144 150Q164 140 186 150L194 236Q166 244 136 236Z")
_bugsy_body = union(
    _bugsy_torso,
    oval(164, 112, 36, 29),  # the head
    svgpath("M180 96Q228 106 252 128Q226 140 182 136Z"),  # the long pointed snout
    oval(124, 88, 24, 24),  # big round ears
    oval(202, 82, 20, 20),
    stroked(svgpath("M150 238L148 252M180 238L184 252"), 9),  # skinny legs
    oval(142, 251, 14, 5),  # feet
    oval(190, 251, 14, 5),
    stroked(svgpath("M144 160Q128 194 144 214"), 8),  # arms, hands in the pockets
    stroked(svgpath("M186 160Q202 194 186 214"), 8),
    stroked(svgpath("M138 230C88 246 62 218 74 186C82 164 108 168 104 188"), 6),  # the curling tail
)


def _bugsy_details(cv: skia.Canvas, status: str) -> None:
    """The flat cap, faint shirt stripes and a red nose tip."""
    cap = skia.Paint(AntiAlias=True)
    cap.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 64), skia.Point(0, 98)], [color("#a8a59c"), color("#5e5c57")]))
    edge = paint("#141418", stroke=2.5)
    crown = svgpath("M130 94Q132 68 164 66Q196 66 206 86L230 92Q224 100 204 98L132 98Z")
    cv.drawPath(crown, cap)
    cv.drawPath(crown, edge)
    cv.drawPath(svgpath("M204 89Q186 92 164 91"), paint("#46443f", stroke=2))  # the brim seam
    cv.save()
    cv.clipPath(_bugsy_torso, doAntiAlias=True)
    for y in range(162, 236, 13):
        cv.drawPath(svgpath(f"M130 {y}L200 {y}"), paint("#30303a", stroke=4))
    cv.restore()
    cv.drawPath(oval(251, 128, 4, 4), paint(BLOOD))


BUGSY = Critter(
    shape=_bugsy_body,
    eyes=[(154, 114), (186, 112)],
    mouth=(214, 136),
    eye=8.5,
    folds=[svgpath("M192 128Q220 134 246 132")],  # the jaw line
    lines=[  # whiskers off the snout
        (svgpath("M234 124L276 112"), 2),
        (svgpath("M236 130L280 136"), 2),
    ],
    details=_bugsy_details,
)

# ---- louie: a plump street pigeon in a newsboy cap -------------------------------------

_louie_body = union(
    oval(156, 186, 62, 58),  # the plump chest
    oval(172, 114, 32, 30),  # the small head
    svgpath("M146 132Q172 146 198 132L204 168L140 168Z"),  # the neck
    poly((200, 106), (228, 118), (200, 128)),  # a short beak
    poly((104, 196), (56, 230), (62, 242), (76, 236), (78, 250), (114, 224)),  # tail feathers
    stroked(svgpath("M142 236L140 252M172 236L174 252"), 6),  # little legs
    stroked(svgpath("M126 253L150 253M162 253L188 253"), 4.5),  # toes
)


def _louie_details(cv: skia.Canvas, status: str) -> None:
    """The puffy newsboy cap with a short visor and a button on top."""
    cap = skia.Paint(AntiAlias=True)
    cap.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 64), skia.Point(0, 104)], [color("#c4c0b6"), color("#7a7871")]))
    edge = paint("#141418", stroke=2.5)
    crown = svgpath("M138 100C126 78 150 62 176 64C204 64 218 80 206 100Z")
    visor = svgpath("M194 92Q222 90 232 100Q218 108 192 104Z")
    for p in (crown, visor):
        cv.drawPath(p, cap)
        cv.drawPath(p, edge)
    cv.drawPath(svgpath("M176 66Q166 82 166 98M176 66Q192 80 196 98"), paint("#66645e", stroke=1.8))  # panels
    cv.drawPath(oval(176, 66, 4, 3.5), paint("#2a2a30"))


LOUIE = Critter(
    shape=_louie_body,
    eyes=[(160, 116), (188, 114)],
    mouth=(204, 132),
    eye=8,
    folds=[
        svgpath("M146 144Q172 154 198 142"),  # the neck ruff
        svgpath("M110 162Q150 182 146 232"),  # folded wing
        svgpath("M110 162Q98 202 120 230"),
    ],
    details=_louie_details,
)

# ---- slick: a raccoon thief in a striped sweater, a loot sack over the shoulder --------

_slick_rings = union(*(stroked(svgpath(f"M{x - 18} {y - 6}L{x + 18} {y + 6}"), 3.5)
                       for x, y in ((238, 210), (247, 182), (240, 156))))
_slick_tail = cut(stroked(svgpath("M196 232C236 236 252 208 246 176C242 156 236 146 232 136"), 26), _slick_rings)
_slick_sweater = svgpath("M120 160Q160 146 200 160L210 240Q160 248 110 240Z")
_slick_head = union(
    oval(160, 124, 42, 32),
    poly((120, 128), (104, 146), (130, 146)),  # cheek fluff
    poly((200, 128), (216, 146), (190, 146)),
)
_slick_sack = union(
    svgpath("M108 124C80 118 68 142 74 166C68 190 88 210 112 204C130 198 134 180 128 164"
            "C134 146 128 128 108 124Z"),  # the lumpy sack over the left shoulder
    poly((100, 126), (92, 104), (106, 114), (114, 100), (120, 126)),  # the gathered top
)
_slick_arm = stroked(svgpath("M136 168Q124 146 112 126"), 12)  # the arm gripping the sack neck
_slick_body = union(
    _slick_sweater,
    _slick_head,
    oval(130, 96, 13, 15),  # small round ears
    oval(190, 96, 13, 15),
    oval(138, 249, 18, 7),  # feet
    oval(182, 249, 18, 7),
    _slick_tail,
    _slick_sack,
    _slick_arm,
)


def _slick_details(cv: skia.Canvas, status: str) -> None:
    """Sweater stripes, the burlap sack behind the head, and the pale face band around the mask."""
    cv.save()
    cv.clipPath(_slick_sweater, doAntiAlias=True)
    for y in range(176, 240, 14):
        cv.drawPath(svgpath(f"M104 {y}L216 {y}"), paint("#2e2e36", stroke=6))
    cv.restore()
    sack = skia.Paint(AntiAlias=True)
    sack.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 100), skia.Point(0, 206)], [color("#7c7970"), color("#34332f")]))
    cv.save()
    cv.clipPath(_slick_head, skia.ClipOp.kDifference, True)
    cv.drawPath(_slick_sack, sack)
    cv.drawPath(_slick_sack, paint("#141418", stroke=2.5))
    cv.drawPath(svgpath("M80 162Q96 170 110 160M92 184Q106 194 120 186"), paint("#2a2926", stroke=2))  # lumps
    cv.restore()
    cv.drawPath(svgpath("M98 124Q110 130 122 122"), paint(INK, stroke=4))  # the rope tie
    cv.drawPath(_slick_arm, paint(INK))
    cv.drawPath(svgpath("M122 126Q122 104 160 104Q198 104 198 126Q198 150 160 152Q122 150 122 126Z"),
                paint("#8c8a84"))
    mask = svgpath("M118 124Q130 108 150 116L160 122L170 116Q190 108 202 124Q196 140 176 136L160 130"
                   "L144 136Q124 140 118 124Z")
    cv.drawPath(mask, paint(INK))
    cv.drawPath(svgpath("M160 108L160 118"), paint(INK, stroke=4))  # the stripe on the brow
    cv.drawPath(oval(160, 140, 5, 3.5), paint(INK))  # the nose


SLICK = Critter(
    shape=_slick_body,
    eyes=[(142, 124), (178, 124)],
    mouth=(160, 146),
    eye=8,
    details=_slick_details,
)

SPRITES = {"bugsy": BUGSY, "louie": LOUIE, "slick": SLICK}
