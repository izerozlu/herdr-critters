"""Batch C: dutch the bulldog, velma the moth, rocco the bat."""

import skia

from .kit import BLOOD, Critter, oval, paint, poly, stroked, svgpath, union

# ---- dutch: a bulldog cop in a peaked cap, heavy jowls, short bowed legs ---------------

_dutch_body = union(
    svgpath("M98 168Q160 150 222 168Q250 198 238 240L82 240Q70 198 98 168Z"),  # the barrel chest
    oval(84, 196, 17, 28),  # stubby arms
    oval(236, 196, 17, 28),
    stroked(svgpath("M132 228Q116 238 122 246M188 228Q204 238 198 246"), 20),  # bowed legs
    oval(118, 249, 20, 7),  # boots
    oval(202, 249, 20, 7),
    stroked(svgpath("M240 212L266 248"), 8),  # the nightstick
)
_dutch_head = union(
    svgpath("M108 112Q112 96 160 96Q208 96 212 112L226 150Q226 176 198 174Q178 170 160 176"
            "Q142 170 122 174Q94 176 94 150Z"),  # a broad flat head, the jowls hanging low
    poly((110, 110), (94, 104), (100, 126)),  # small folded ears
    poly((210, 110), (226, 104), (220, 126)),
)
_dutch_cap = union(
    svgpath("M108 84Q104 60 160 56Q216 60 212 84Z"),  # the flat top, wider than the band
    poly((122, 80), (198, 80), (198, 100), (122, 100)),  # band
    svgpath("M116 98Q160 112 204 98L200 108Q160 120 120 108Z"),  # visor
)


def _dutch_details(cv: skia.Canvas, status: str) -> None:
    """The pale cap badge, the nose shine and the brass buttons."""
    cv.drawPath(poly((160, 66), (170, 72), (168, 86), (160, 92), (152, 86), (150, 72)), paint("#d8d2c2"))
    cv.drawPath(oval(160, 78, 3, 3), paint("#6a675f"))
    cv.drawPath(oval(160, 142, 11, 6), paint("#2a2a32"))  # the broad nose
    cv.drawPath(oval(156, 140, 3.5, 2), paint("#9a9aa4"))
    tooth = paint("#ece6d6")
    cv.drawPath(poly((146, 166), (151, 166), (149, 159)), tooth)  # the underbite
    cv.drawPath(poly((169, 166), (174, 166), (171, 159)), tooth)
    for y in (182, 202, 222):
        cv.drawPath(oval(160, y, 3.2, 3.2), paint("#c8c2b2"))
    cv.drawPath(poly((190, 184), (194, 192), (190, 198), (186, 192)), paint("#a8a294"))  # chest shield


DUTCH = Critter(
    shape=union(_dutch_body, _dutch_head, _dutch_cap),
    eyes=[(140, 124), (180, 124)],
    mouth=(160, 160),
    eye=8.5,
    folds=[
        svgpath("M124 80L196 80"),  # cap band edge
        svgpath("M128 150Q144 162 160 152Q176 162 192 150"),  # the jowl line
        svgpath("M96 212Q160 220 224 212"),  # belt
        svgpath("M146 168L160 176L174 168"),  # collar
    ],
    details=_dutch_details,
)

# ---- velma: a moth in a long gown, wings spread wide, red lips ------------------------


def _plume(x0: float, y0: float, x1: float, y1: float) -> skia.Path:
    """A feathery antenna: a stem from (x0, y0) to (x1, y1), combed with barbs widest in the middle."""
    dx, dy = x1 - x0, y1 - y0
    n = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / n, dy / n
    d = f"M{x0} {y0}L{x1} {y1}"
    for i in range(1, 9):
        t = i / 9
        bx, by, ln = x0 + dx * t, y0 + dy * t, 4 + 6 * (1 - abs(t - 0.5) * 2)
        for side in (1, -1):  # both sides, raked toward the tip
            d += f"M{bx} {by}L{bx + (-uy * side + ux * 0.6) * ln} {by + (ux * side + uy * 0.6) * ln}"
    return stroked(svgpath(d), 2.6)


_velma_wings = union(
    svgpath("M156 146C120 96 72 98 54 122C44 148 82 176 152 168Z"),  # upper wings
    svgpath("M164 146C200 96 248 98 266 122C276 148 238 176 168 168Z"),
    svgpath("M154 166C112 170 80 196 88 224C96 244 132 232 156 192Z"),  # lower wings
    svgpath("M166 166C208 170 240 196 232 224C224 244 188 232 164 192Z"),
)
_velma_body = union(
    oval(160, 120, 26, 22),  # head
    oval(160, 152, 16, 20),  # thorax
    svgpath("M148 164Q144 216 124 254L196 254Q176 216 172 164Z"),  # the long gown
    _plume(152, 102, 116, 56),  # feathery antennae
    _plume(168, 102, 204, 56),
)


def _velma_details(cv: skia.Canvas, status: str) -> None:
    """Pale eyespots on the wings and small red lips."""
    for x, y, r in ((96, 132, 13), (224, 132, 13), (112, 210, 8), (208, 210, 8)):
        cv.drawPath(oval(x, y, r, r), paint("#b8b4aa"))
        cv.drawPath(oval(x, y, r * 0.55, r * 0.55), paint("#060608"))
        cv.drawPath(oval(x - r * 0.2, y - r * 0.2, r * 0.18, r * 0.18), paint("#e8e4d8"))
    cv.drawPath(svgpath("M153 134Q157 131 160 133Q163 131 167 134Q160 140 153 134Z"), paint(BLOOD))


VELMA = Critter(
    shape=union(_velma_wings, _velma_body),
    eyes=[(149, 118), (171, 118)],
    mouth=(160, 136),
    eye=8,
    folds=[
        svgpath("M150 150Q110 120 66 124M150 156Q110 150 70 150"),  # wing veins
        svgpath("M170 150Q210 120 254 124M170 156Q210 150 250 150"),
        svgpath("M152 178Q120 196 98 220M168 178Q200 196 222 220"),
        svgpath("M150 200Q160 206 170 200"),  # gown waist
    ],
    details=_velma_details,
)

# ---- rocco: a bat in a fedora, wings wrapped like a cloak, pale fangs -----------------

_rocco_cloak = svgpath(
    "M134 146Q160 140 186 146L200 140L206 160Q232 196 244 240"
    "Q230 226 220 248Q208 230 196 254Q184 236 172 256Q160 238 148 256"
    "Q136 236 124 254Q112 230 100 248Q90 226 76 240Q88 196 114 160L120 140Z"
)  # tall and wide, the scalloped wing edge along the bottom
_rocco_head = union(
    oval(160, 124, 30, 26),
    poly((136, 112), (100, 40), (154, 98)),  # big pointed ears, past the brim
    poly((184, 112), (220, 40), (166, 98)),
)
_rocco_hat = union(
    oval(160, 94, 50, 8),
    svgpath("M138 96L142 70Q152 64 160 68Q168 64 178 70L182 96Z"),
)
_rocco_claws = union(
    poly((116, 146), (108, 128), (124, 142)),  # wing thumbs over the shoulders
    poly((204, 146), (212, 128), (196, 142)),
)


def _rocco_details(cv: skia.Canvas, status: str) -> None:
    """Two pale fangs."""
    fang = paint("#ece6d6")
    cv.drawPath(poly((152, 140), (157, 140), (154.5, 148)), fang)
    cv.drawPath(poly((163, 140), (168, 140), (165.5, 148)), fang)


ROCCO = Critter(
    shape=union(_rocco_cloak, _rocco_head, _rocco_hat, _rocco_claws),
    eyes=[(147, 122), (173, 122)],
    mouth=(160, 140),
    eye=8,
    folds=[
        svgpath("M140 84L180 84"),  # hat band
        svgpath("M160 150L124 254M160 150L172 256M160 150L222 248"),  # wing fingers
        svgpath("M160 150L98 248M160 150L196 254"),
    ],
    details=_rocco_details,
)

SPRITES = {"dutch": DUTCH, "velma": VELMA, "rocco": ROCCO}
