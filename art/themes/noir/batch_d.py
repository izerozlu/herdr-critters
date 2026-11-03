"""Batch D: lefty the dog, mickey the mouse, dolly the fox."""

import skia

from .kit import BLOOD, INK, Critter, color, oval, paint, poly, stroked, svgpath, union

# ---- lefty: a one-eyed alley dog in a leather jacket, a patch over the left eye -------

_lefty_body = union(
    svgpath("M108 162Q160 144 212 162L224 230Q160 238 96 230Z"),  # the jacket, cut short
    poly((110, 164), (122, 138), (146, 160)),  # the collar points
    poly((210, 164), (198, 138), (174, 160)),
    stroked(svgpath("M136 228L134 246M184 228L186 246"), 24),  # legs
    oval(132, 250, 18, 7),  # paws
    oval(188, 250, 18, 7),
)
_lefty_head = union(
    oval(154, 112, 42, 36),
    svgpath("M176 98Q222 92 236 114Q240 134 220 142Q192 148 170 134Z"),  # the long muzzle
    oval(235, 112, 8, 7),  # the nose
    svgpath("M124 86Q98 80 88 112Q82 150 98 172Q114 162 122 140Q130 116 134 96Z"),  # floppy ears
    svgpath("M176 80Q202 70 214 92Q208 104 196 102Q186 92 176 92Z"),
)
_lefty_tail = stroked(svgpath("M98 218Q72 208 74 180"), 12)


def _lefty_details(cv: skia.Canvas, status: str) -> None:
    """The eye patch and its strap, the studded collar and the jacket zipper."""
    strap = paint("#76767e", stroke=2.5)
    cv.drawPath(svgpath("M150 102Q164 86 178 78"), strap)  # over the brow, behind the ear
    cv.drawPath(svgpath("M126 116Q120 112 112 108"), strap)
    patch = svgpath("M128 104Q142 98 154 104Q156 122 141 126Q128 122 128 104Z")
    cv.drawPath(patch, paint("#16161a"))
    cv.drawPath(patch, paint("#8a8a92", stroke=2))
    cv.drawPath(svgpath("M122 152Q160 164 198 150"), paint("#26262c", stroke=8))  # the collar
    for x, y in ((130, 155), (145, 159), (160, 160), (175, 158), (190, 153)):
        cv.drawPath(oval(x, y, 2.8, 2.8), paint("#d8d4c8"))
    cv.drawPath(svgpath("M160 168L160 230"), paint("#b4b0a6", stroke=2))  # the zipper
    cv.drawPath(poly((156.5, 174), (163.5, 174), (162.5, 184), (157.5, 184)), paint("#d8d4c8"))  # its pull


LEFTY = Critter(
    shape=union(_lefty_body, _lefty_head, _lefty_tail),
    eyes=[(180, 108)],
    mouth=(212, 136),
    eye=9.5,
    folds=[
        svgpath("M198 134Q216 138 228 128"),  # the jaw line
        svgpath("M104 210Q160 218 216 210"),  # the jacket waistband
        svgpath("M110 176Q118 200 112 226M210 176Q202 200 208 226"),  # sleeves
        svgpath("M136 166L142 196M184 166L178 196"),  # lapel seams
    ],
    details=_lefty_details,
)

# ---- mickey: a small mouse newsboy in a cap, holding up the late edition --------------

_mickey_body = union(
    oval(160, 128, 34, 30),
    poly((186, 132), (212, 146), (184, 148)),  # the pointed snout
    oval(120, 92, 27, 27),  # very big round ears
    oval(200, 92, 27, 27),
    svgpath("M130 160Q160 150 190 160L198 236Q160 244 122 236Z"),  # the small body
    stroked(svgpath("M144 236L142 248M176 236L178 248"), 12),  # legs
    stroked(svgpath("M136 168Q114 176 112 198M184 168Q206 174 208 192"), 9),  # arms up to the paper
    oval(138, 251, 13, 5),  # shoes
    oval(182, 251, 13, 5),
    stroked(svgpath("M196 230C232 238 248 214 238 196C232 186 240 176 250 180"), 4),  # thin tail
)
def _mickey_details(cv: skia.Canvas, status: str) -> None:
    """The pale tweed cap, and the pale newspaper held up in both paws, EXTRA on top."""
    tweed = skia.Paint(AntiAlias=True)
    tweed.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 78), skia.Point(0, 112)], [color("#d4d0c4"), color("#86837b")]))
    edge = paint("#141418", stroke=2.5)
    crown = svgpath("M122 108Q120 80 158 78Q196 78 202 102Q170 98 122 108Z")  # soft, puffed crown
    brim = svgpath("M176 104Q206 96 218 108Q206 116 182 114Z")  # the short brim, tipped forward
    for p in (crown, brim):
        cv.drawPath(p, tweed)
        cv.drawPath(p, edge)
    cv.drawPath(svgpath("M160 80Q150 92 142 104M160 80Q172 90 178 102"), paint("#6e6b64", stroke=1.6))  # panels
    cv.drawPath(oval(160, 80, 4, 3), paint("#3a3a40"))  # the button
    sheet = skia.Paint(AntiAlias=True)
    sheet.setShader(skia.GradientShader.MakeLinear(
        [skia.Point(0, 170), skia.Point(0, 232)], [color("#e4e0d4"), color("#9c998f")]))
    page = poly((112, 172), (204, 166), (208, 228), (116, 234))
    cv.drawPath(page, sheet)
    cv.drawPath(page, paint("#141418", stroke=2.5))
    ink = paint("#1a1a1e", stroke=3, cap=skia.Paint.kButt_Cap)
    extra = ("M124 176L122 192M124 176L132 176M123 184L130 184M122 192L130 192"  # E
             "M136 176L144 191M144 176L136 191"  # X
             "M148 176L156 176M152 176L152 190"  # T
             "M160 175L159 190M160 175Q168 176 166 182Q164 184 160 183L167 189"  # R
             "M170 189L174 174L180 188M171 184L178 183")  # A
    cv.drawPath(svgpath(extra), ink)
    thin = paint("#4a4a52", stroke=2, cap=skia.Paint.kButt_Cap)
    for i in range(4):
        y = 202 + i * 7
        cv.drawPath(svgpath(f"M124 {y + 0.4}L156 {y - 1}"), thin)
        cv.drawPath(svgpath(f"M164 {y - 1.3}L198 {y - 2.6}"), thin)
    cv.drawPath(svgpath("M120 196L200 192"), paint("#1a1a1e", stroke=2))  # rule under the headline
    for x, y in ((112, 200), (208, 194)):  # the paws gripping the sides
        cv.drawPath(oval(x, y, 9, 8), paint(INK))


MICKEY = Critter(
    shape=_mickey_body,
    eyes=[(148, 126), (176, 126)],
    mouth=(166, 148),
    eye=7.5,
    lines=[  # whiskers past the snout
        (svgpath("M196 142L228 134"), 2),
        (svgpath("M196 146L230 148"), 2),
    ],
    details=_mickey_details,
)

# ---- dolly: a fox lounge singer in a long gown, a rose by her ear --------------------

_dolly_body = union(
    oval(160, 118, 34, 29),
    poly((132, 116), (108, 134), (136, 140)),  # cheek fluff
    poly((188, 116), (212, 134), (184, 140)),
    svgpath("M144 128Q160 156 176 128Z"),  # the narrow muzzle
    poly((134, 104), (124, 44), (156, 94)),  # tall pointed ears
    poly((186, 104), (196, 44), (164, 94)),
    svgpath("M134 150Q160 138 186 150Q188 176 174 198Q192 236 208 254L112 254Q128 236 146 198"
            "Q132 176 134 150Z"),  # the slim gown, flaring at the hem
    svgpath("M130 252C92 254 72 232 80 200C86 176 108 168 118 182C126 194 114 206 106 204"
            "C100 220 112 236 134 236Z"),  # the bushy tail, curled to her left
)


def _dolly_details(cv: skia.Canvas, status: str) -> None:
    """The red rose by her ear, the lashes and the sequin sparkle on the gown."""
    cv.drawPath(oval(195, 100, 10, 9), paint(BLOOD))
    cv.drawPath(svgpath("M190 99Q195 94 199 100Q194 104 191 101"), paint("#8a1820", stroke=1.6))
    cv.drawPath(poly((200, 108), (210, 110), (204, 104)), paint("#3a4a3a"))  # a leaf
    lash = paint("#8e8e98", stroke=1.8)
    for x, side in ((146, -1), (174, 1)):
        for k in range(3):
            cv.drawPath(svgpath(f"M{x + side * (5 + k * 2.5)} {112 - k * 0.5}"
                                f"L{x + side * (9 + k * 3.5)} {106 - k * 1.5}"), lash)
    sequins = ((150, 212), (166, 222), (140, 232), (176, 238), (156, 244), (190, 248), (128, 248),
               (162, 202), (146, 226))
    for x, y in sequins:
        cv.drawPath(oval(x, y, 1.6, 1.6), paint("#efe9da"))
    for x, y in ((170, 226), (136, 244)):  # two catch the light
        cv.drawPath(oval(x, y, 4, 4), paint("#fff6e0", 0.5, blur=2))
        cv.drawPath(svgpath(f"M{x - 4} {y}L{x + 4} {y}M{x} {y - 4}L{x} {y + 4}"), paint("#fbf6ea", stroke=1.4))


DOLLY = Critter(
    shape=_dolly_body,
    eyes=[(146, 116), (174, 116)],
    mouth=(160, 140),
    eye=8,
    pupil="slit",
    folds=[
        svgpath("M140 154Q160 166 180 154"),  # the neckline
        svgpath("M160 196Q154 226 150 252"),  # a slit in the gown
        svgpath("M96 210Q92 228 112 240"),  # the tail's curl
    ],
    details=_dolly_details,
)

SPRITES = {"lefty": LEFTY, "mickey": MICKEY, "dolly": DOLLY}
