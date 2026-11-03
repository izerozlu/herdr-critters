"""Sprites batch A: onigiri, sushi, dango, mochi, ramen, tofu, taiyaki, matcha, gyoza, bento."""

from .kit import INK, PAPER, circle, ellipse, path, rect

NORI = "#26302a"
GRAIN = "#e2dac4"
INDIGO, VERMILION, OCHRE, MATCHA = "#2d4a7a", "#c23b22", "#c89a3a", "#8fb050"
SAKURA, WOOD = "#e8a0b0", "#a8713e"
SALMON, TOFU, BROTH = "#f0906a", "#e6e0cc", "#d9a860"

# Per sprite: the body, drawn back to front.
SPRITES: dict[str, str] = {
    "onigiri": (
        path("M80 18 Q90 18 96 30 L126 102 Q132 122 112 122 L48 122 Q28 122 34 102 L64 30 Q70 18 80 18 Z", PAPER)
        + path("M70 34 Q76 26 84 28", stroke=GRAIN, width=4)
        + "".join(ellipse(x, y, 3, 1.6, GRAIN, None) for x, y in ((74, 46), (90, 50), (60, 80), (100, 78), (82, 40)))
        + rect(48, 88, 64, 34, NORI, 3)
        + path("M54 96 L106 96", stroke="#3c4a40", width=2.5)
    ),
    "sushi": (
        rect(42, 82, 76, 40, PAPER, 14)
        + path("M60 96 L60 108 M80 98 L80 112 M100 96 L100 108", stroke=GRAIN, width=3)
        + path("M34 88 Q32 54 80 50 Q128 54 126 88 Q80 100 34 88 Z", SALMON)
        + path("M46 64 Q64 56 76 58 M92 58 Q106 58 116 66", stroke=PAPER, width=4)
    ),
    "dango": (
        rect(77, 0, 6, 18, WOOD, 2, INK, 3)
        + circle(80, 104, 21, MATCHA)
        + circle(80, 69, 21, PAPER)
        + circle(80, 32, 21, SAKURA)
        + path("M68 24 Q72 18 80 17", stroke=PAPER, width=3.5)
    ),
    "mochi": (
        path("M36 108 Q34 72 80 70 Q126 72 124 108 Q126 122 108 122 L52 122 Q34 122 36 108 Z", PAPER)
        + path("M54 76 Q52 46 80 46 Q108 46 106 76 Q80 86 54 76 Z", PAPER)
        + path("M80 28 Q86 20 94 22 Q90 30 80 28 Z", MATCHA, INK, 3)
        + circle(80, 38, 11, "#e07a28")
        + path("M72 34 Q75 30 80 30", stroke=PAPER, width=3)
    ),
    "ramen": (
        path("M42 76 Q42 44 80 44 Q118 44 118 76 Z", "#f0e2b0")
        + path("M52 66 Q60 56 68 66 T84 66 T100 66 T112 62", stroke=OCHRE, width=3)
        + path("M52 56 Q62 48 70 56 T88 54", stroke=OCHRE, width=3)
        + ellipse(98, 56, 14, 11, PAPER, INK, 4)
        + circle(98, 56, 5.5, OCHRE, None)
        + path("M72 66 L118 12 M82 70 L128 18", stroke=INK, width=9)
        + path("M72 66 L118 12 M82 70 L128 18", stroke=WOOD, width=4)
        + path("M28 74 L132 74 Q134 122 80 122 Q26 122 28 74 Z", INDIGO)
        + path("M34 80 L126 80", stroke=BROTH, width=4)
    ),
    "tofu": (
        path("M36 62 L58 42 L132 42 L110 62 Z", PAPER)
        + path("M110 62 L132 42 L132 102 L110 122 Z", TOFU)
        + path("M36 62 L110 62 L110 122 L36 122 Z", PAPER)
        + path("M46 66 L100 66", stroke=GRAIN, width=3)
        + path("M80 46 Q84 38 90 36 M88 46 Q96 40 100 34", stroke=MATCHA, width=4)
    ),
    "taiyaki": (
        path("M34 90 Q34 56 76 56 Q98 56 108 76 L128 56 Q134 90 128 122 L108 102 Q98 122 76 122 Q34 122 34 90 Z", "#e0a850")
        + path("M94 82 Q102 90 94 98 M104 92 Q110 98 104 106 M92 104 Q98 110 92 116", stroke=WOOD, width=3.5)
        + path("M114 76 L122 70 M116 90 L124 90 M114 104 L122 110", stroke=WOOD, width=3.5)
        + path("M44 70 Q56 62 70 64", stroke="#f2cc84", width=4)
    ),
    "matcha": (
        path("M30 66 L130 66 Q128 122 100 122 L60 122 Q32 122 30 66 Z", "#e8c9a0")
        + path("M52 122 L108 122", stroke=WOOD, width=6)
        + ellipse(80, 66, 50, 14, MATCHA)
        + "".join(circle(x, y, r, "#b6d07a", None) for x, y, r in ((62, 64, 6), (82, 70, 5), (98, 62, 6), (74, 60, 3)))
    ),
    "gyoza": (
        path("M28 98 Q40 56 80 54 Q120 56 132 98 Q112 124 80 122 Q48 124 28 98 Z", "#ecd9a8")
        + path("M34 104 Q80 128 126 104 Q110 120 80 120 Q50 120 34 104 Z", OCHRE, None)
        + path("M28 98 Q40 56 80 54 Q120 56 132 98 Q112 124 80 122 Q48 124 28 98 Z")
        + path("M50 64 L54 76 M66 58 L68 70 M82 56 L82 68 M98 58 L96 70 M112 64 L108 76", stroke=WOOD, width=3.5)
    ),
    "bento": (
        path("M38 80 Q36 52 60 50 Q80 50 80 66 L80 80 Z", PAPER)
        + circle(58, 62, 7, VERMILION, INK, 3)
        + rect(80, 56, 40, 26, "#e8c050", 6, INK, 4)
        + path("M88 62 L88 76 M100 62 L100 76", stroke=OCHRE, width=3)
        + circle(106, 52, 10, MATCHA, INK, 4)
        + rect(30, 76, 100, 46, VERMILION, 8)
        + rect(42, 84, 76, 32, PAPER, 5, INK, 3)
    ),
}

# Per sprite: the face (see kit.face) and optional extra shapes per status.
POSES: dict[str, dict] = {
    "onigiri": {
        "eyes": [(66, 62), (94, 62)], "mouth": (80, 76), "blush": [(54, 74), (106, 74)],
        "working": path("M80 18 Q84 8 92 10", stroke=INK, width=2.5),
    },

    "sushi": {"eyes": [(66, 70), (94, 70)], "mouth": (80, 82), "blush": [(54, 80), (106, 80)]},
    "dango": {"eyes": [(68, 68), (92, 68)], "mouth": (80, 80), "blush": []},
    "mochi": {
        "eyes": [(64, 96), (96, 96)], "mouth": (80, 108), "blush": [(52, 106), (108, 106)],
        "working": path("M80 22 Q84 12 92 14", stroke=INK, width=2.5),
    },
    "ramen": {
        "eyes": [(64, 96), (96, 96)], "mouth": (80, 108), "blush": [(50, 106), (110, 106)], "ink": PAPER,
        "working": path("M50 40 Q44 30 50 22 M72 36 Q66 26 72 18", stroke=INK, width=2.5),
    },
    "tofu": {"eyes": [(61, 88), (87, 88)], "mouth": (74, 101), "blush": [(48, 98), (100, 98)]},
    "taiyaki": {"eyes": [(50, 88), (78, 88)], "mouth": (64, 100), "blush": [(40, 98), (88, 98)]},
    "matcha": {
        "eyes": [(64, 92), (96, 92)], "mouth": (80, 104), "blush": [(50, 102), (110, 102)],
        "working": path("M62 46 Q56 36 62 28 M98 46 Q92 36 98 28", stroke=INK, width=2.5),
    },
    "gyoza": {
        "eyes": [(64, 88), (96, 88)], "mouth": (80, 100), "blush": [(50, 98), (110, 98)],
        "working": path("M60 44 Q54 34 60 26 M100 44 Q94 34 100 26", stroke=INK, width=2.5),
    },
    "bento": {"eyes": [(66, 98), (94, 98)], "mouth": (80, 108), "blush": []},
}
