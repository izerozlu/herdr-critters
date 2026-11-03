"""Batch A: spade the alley cat, vito the crow, marlow the owl."""

import skia

from .kit import BLOOD, INK, Critter, color, cut, oval, paint, poly, stroked, svgpath, union

# ---- spade: an alley cat in a fedora and a trench coat, ears through the brim ----------

_spade_coat = union(
    svgpath("M110 160Q160 142 210 160L228 246Q160 254 92 246Z"),
    poly((110, 162), (122, 126), (144, 160)),  # the turned-up collar
    poly((210, 162), (198, 126), (176, 160)),
    oval(138, 250, 17, 7),  # boots
    oval(182, 250, 17, 7),
)
_spade_head = cut(union(
    oval(160, 122, 42, 33),
    poly((122, 124), (106, 142), (128, 148)),  # cheek fluff
    poly((198, 124), (214, 142), (192, 148)),
    svgpath("M112 104Q96 76 100 50Q124 56 148 82Z"),  # broad cat ears, out past the brim
    svgpath("M208 104Q224 76 220 50Q196 56 172 82Z"),
), poly((94, 62), (108, 67), (96, 73)))  # a torn notch: an alley cat
_spade_hat = union(
    oval(160, 86, 70, 10),
    svgpath("M131 88L136 54Q148 46 160 52Q172 46 184 54L189 88Z"),
)
_spade_tail = stroked(svgpath("M212 238C252 238 264 210 254 182C248 164 256 150 268 152"), 13)

SPADE = Critter(
    shape=union(_spade_coat, _spade_head, _spade_hat, _spade_tail),
    eyes=[(143, 120), (177, 120)],
    mouth=(160, 140),
    eye=8.5,
    pupil="slit",
    folds=[
        svgpath("M144 162L160 196L176 162"),  # lapels
        svgpath("M102 206Q160 214 218 206"),  # belt
        svgpath("M160 214L160 244"),
        svgpath("M132 77L188 77"),  # hat band
    ],
    lines=[  # whiskers past the cheeks
        (svgpath("M122 132L82 124"), 2.2),
        (svgpath("M124 138L80 142"), 2.2),
        (svgpath("M198 132L238 124"), 2.2),
        (svgpath("M196 138L240 142"), 2.2),
    ],
)

# ---- vito: a crow in a pale fedora and a red tie, beak in profile ---------------------

_vito_body = union(
    oval(150, 196, 54, 52),
    oval(162, 120, 38, 36),
    svgpath("M188 104Q226 110 248 130Q222 138 190 140Z"),  # the beak
    poly((106, 212), (64, 252), (86, 254), (116, 236)),  # tail feathers
    poly((128, 108), (108, 102), (126, 128)),  # a ruffled nape
    stroked(svgpath("M140 236L138 254M164 236L166 254"), 6),  # legs
    stroked(svgpath("M126 254L150 254M152 254L178 254"), 5),  # toes
)


def _vito_details(cv: skia.Canvas, status: str) -> None:
    """The pale fedora with a black band, a pale collar and the red tie."""
    hat = skia.Paint(AntiAlias=True)
    hat.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 44), skia.Point(0, 96)], [color("#dcd8cc"), color("#8c8981")]))
    edge = paint("#141418", stroke=2.5)
    crown = svgpath("M128 86L134 52Q148 43 162 50Q176 43 190 52L196 86Z")
    brim = svgpath("M94 90Q104 76 162 78Q220 76 232 88Q222 98 162 96Q104 98 94 90Z")
    for p in (crown, brim):
        cv.drawPath(p, hat)
        cv.drawPath(p, edge)
    cv.drawRect(skia.Rect.MakeLTRB(130.5, 72, 194.5, 82), paint("#16161a"))
    cv.drawPath(svgpath("M146 50Q156 56 162 50"), paint("#7e7b74", stroke=2))  # the pinch
    collar = paint("#9c998f")
    cv.drawPath(poly((142, 150), (160, 156), (150, 168)), collar)
    cv.drawPath(poly((180, 150), (162, 156), (172, 168)), collar)
    cv.drawPath(poly((155, 156), (167, 156), (165, 166), (157, 166)), paint(BLOOD))
    cv.drawPath(poly((157, 166), (165, 166), (171, 200), (161, 212), (151, 200)), paint(BLOOD))
    cv.drawPath(svgpath("M161 168L160 206"), paint("#8a1820", stroke=1.6))


VITO = Critter(
    shape=_vito_body,
    eyes=[(148, 122), (176, 120)],
    mouth=(186, 146),
    eye=7.5,
    folds=[
        svgpath("M196 128Q220 131 240 130"),  # the beak line
        svgpath("M114 172Q150 186 142 236"),  # folded wing
        svgpath("M114 172Q100 204 118 234"),
    ],
    details=_vito_details,
)

# ---- marlow: an owl detective with ear tufts and a magnifying glass -------------------

_marlow_body = union(
    svgpath("M118 92L150 88L160 98L170 88L202 92C220 104 224 140 224 180C222 230 200 250 160 250"
            "C120 250 98 230 96 180C96 140 100 104 118 92Z"),  # broad flat head with a V brow
    poly((112, 104), (92, 56), (108, 68), (104, 46), (136, 92)),  # feathered ear tufts
    poly((208, 104), (228, 56), (212, 68), (216, 46), (184, 92)),
    svgpath("M104 140Q78 192 100 242L110 232L112 246L126 236Z"),  # folded wing, feather tips
    oval(140, 251, 15, 6),  # talons
    oval(180, 251, 15, 6),
    stroked(svgpath("M206 192Q232 198 234 178"), 16),  # the wing holding the glass
    stroked(svgpath("M232 184L242 160"), 7),  # handle
    stroked(oval(246, 140, 19, 19), 7),  # lens ring
)
_LENS = {"idle": ("#4c4c56", 0.0), "working": ("#f4f1e8", 0.9), "blocked": (BLOOD, 0.8), "done": ("#d8ceb4", 0.6)}


def _marlow_details(cv: skia.Canvas, status: str) -> None:
    """The beak, and the lens glass lit in the status color."""
    disc = svgpath("M160 156C130 166 108 150 110 126C112 104 136 98 160 112C184 98 208 104 210 126"
                   "C212 150 190 166 160 156Z")  # the heart-shaped facial disc
    cv.drawPath(disc, paint("#34343c", stroke=3))
    cv.drawPath(svgpath("M153 136Q160 132 167 136L161 156Q160 158 159 156Z"), paint("#8c8a92"))  # hooked beak
    hue, glow = _LENS[status]
    if glow:
        cv.drawPath(oval(246, 140, 24, 24), paint(hue, glow * 0.6, blur=8))
    cv.drawPath(oval(246, 140, 16, 16), paint(hue, 0.95 if glow else 1))
    cv.drawPath(svgpath("M236 134Q240 126 248 125"), paint("#ffffff", 0.75 if glow else 0.35, stroke=2.5))
    cv.drawPath(oval(246, 140, 19, 19), paint(INK, stroke=6))


MARLOW = Critter(
    shape=_marlow_body,
    eyes=[(138, 126), (182, 126)],
    mouth=(160, 172),
    eye=11,
    folds=[
        svgpath("M132 194L140 202L148 194M152 194L160 202L168 194M172 194L180 202L188 194"),
        svgpath("M142 214L150 222L158 214M162 214L170 222L178 214"),
        svgpath("M104 160Q112 210 132 236"),  # wing edge
    ],
    details=_marlow_details,
)

SPRITES = {"spade": SPADE, "vito": VITO, "marlow": MARLOW}
