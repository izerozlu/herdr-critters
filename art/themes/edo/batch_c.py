"""Sprites batch C: kokeshi, daruma, chochin, geta, sensu, furin, kendama, torii, kasa, maneki."""

from .kit import INK, PAPER, circle, ellipse, path, rect

VERMILION = "#c23b22"
INDIGO = "#2d4a7a"
OCHRE = "#c89a3a"
GOLD = "#e0b040"
WOOD = "#a8713e"
LIGHT_WOOD = "#d8b07a"
SAKURA = "#e8a0b0"
GLASS = "#a8d0e0"
SKIN = "#f2dcc0"
GLOW = "#f4dca0"

# Per sprite: the body, drawn back to front.
SPRITES: dict[str, str] = {
    "kokeshi": (
        path("M56 68 L52 118 Q52 124 60 124 L100 124 Q108 124 108 118 L104 68 Z", VERMILION)
        + path("M53 100 L107 100", stroke=INK, width=3)
        + circle(80, 86, 7, SAKURA, INK, 3)
        + circle(66, 111, 5, GOLD, INK, 3)
        + circle(94, 111, 5, GOLD, INK, 3)
        + circle(80, 40, 28, SKIN)
        + path("M52 42 Q50 12 80 12 Q110 12 108 42 Q100 28 80 28 Q60 28 52 42 Z", INK, INK, 4)
        + path("M80 28 L80 20", stroke=SKIN, width=3)
    ),
    "daruma": (
        path("M80 28 Q124 28 124 80 Q124 124 80 124 Q36 124 36 80 Q36 28 80 28 Z", VERMILION)
        + ellipse(80, 68, 31, 24, PAPER)
        + path("M52 52 Q62 40 76 50", stroke=INK, width=9)
        + path("M52 52 Q62 40 76 50", stroke=GOLD, width=4)
        + path("M84 50 Q98 40 108 52", stroke=INK, width=9)
        + path("M84 50 Q98 40 108 52", stroke=GOLD, width=4)
        + "".join(path(d, stroke=GOLD, width=4) for d in (
            "M58 104 Q80 96 102 104", "M64 114 Q80 108 96 114", "M48 94 Q52 86 56 94", "M104 94 Q108 86 112 94"))
    ),
    "chochin": (
        path("M80 8 L80 14", stroke=INK, width=4)
        + path("M56 26 Q36 68 56 110 L104 110 Q124 68 104 26 Z", VERMILION)
        + path("M46 46 Q80 54 114 46", stroke=INK, width=3)
        + path("M46 90 Q80 98 114 90", stroke=INK, width=3)
        + ellipse(80, 68, 27, 24, GLOW)
        + rect(54, 14, 52, 14, INK, 3)
        + rect(54, 108, 52, 14, INK, 3)
    ),
    "geta": (
        rect(46, 80, 16, 42, WOOD, 3)
        + rect(98, 80, 16, 42, WOOD, 3)
        + rect(36, 34, 88, 46, LIGHT_WOOD, 12)
        + path("M62 36 Q80 -2 98 36", stroke=INK, width=14)
        + path("M62 36 Q80 -2 98 36", stroke=VERMILION, width=7)
        + path("M44 74 Q80 80 116 74", stroke=WOOD, width=3)
    ),
    "sensu": (
        path("M80 114 L32 60 A72 72 0 0 1 128 60 Z", PAPER)
        + path("M80 114 L32 60", stroke=INK, width=3)
        + path("M80 114 L128 60", stroke=INK, width=3)
        + "".join(path(f"M80 114 L{x} {y}", stroke=OCHRE, width=2.5) for x, y in ((46, 48), (114, 48)))
        + circle(80, 50, 8, VERMILION, None)
        + path("M80 114 L32 60", stroke=WOOD, width=5)
        + path("M80 114 L128 60", stroke=WOOD, width=5)
        + rect(73, 110, 14, 14, WOOD, 4)
        + circle(80, 112, 4, GOLD, INK, 3)
    ),
    "furin": (
        path("M80 6 L80 22", stroke=INK, width=4)
        + path("M80 84 L80 96", stroke=INK, width=3)
        + path("M42 80 Q42 24 80 24 Q118 24 118 80 Q80 90 42 80 Z", GLASS)
        + path("M42 80 Q80 90 118 80 L118 72 Q80 82 42 72 Z", INDIGO, INK, 4)
        + path("M54 40 Q60 30 70 28", stroke=PAPER, width=4)
        + path("M70 96 L90 96 L90 126 L70 126 Z", SAKURA)
        + path("M70 106 L90 106", stroke=VERMILION, width=3)
    ),
    "kendama": (
        path("M70 92 L72 124 L88 124 L90 92 Z", LIGHT_WOOD)
        + path("M80 54 L80 62", stroke=INK, width=4)
        + circle(80, 34, 23, VERMILION)
        + circle(72, 26, 4, PAPER, None)
        + rect(40, 58, 80, 40, LIGHT_WOOD, 14)
        + path("M40 66 Q80 74 120 66", stroke=WOOD, width=3)
        + path("M40 90 Q80 98 120 90", stroke=WOOD, width=3)
    ),
    "torii": (
        rect(42, 46, 14, 76, VERMILION, 2)
        + rect(104, 46, 14, 76, VERMILION, 2)
        + rect(36, 52, 88, 12, VERMILION, 2)
        + rect(58, 36, 44, 56, PAPER, 3)
        + path("M34 24 Q80 44 126 24 L124 38 Q80 56 36 38 Z", INK, INK, 4)
    ),
    "kasa": (
        path("M80 82 L80 112 Q80 124 92 122", stroke=INK, width=13)
        + path("M80 82 L80 112 Q80 124 92 122", stroke=WOOD, width=6)
        + path("M32 80 Q32 28 80 28 Q128 28 128 80 Q104 90 80 82 Q56 90 32 80 Z", "#e6c27a")
        + path("M80 28 L38 80", stroke=VERMILION, width=3)
        + path("M80 28 L122 80", stroke=VERMILION, width=3)
        + path("M34 78 Q56 88 80 80 Q104 88 126 78", stroke=INDIGO, width=5)
        + circle(80, 28, 5, INK, None)
    ),
    "maneki": (
        ellipse(80, 98, 34, 26, PAPER)
        + path("M108 90 Q126 84 122 56", stroke=INK, width=24)
        + path("M108 90 Q126 84 122 56", stroke=PAPER, width=12)
        + circle(121, 46, 11, PAPER)
        + path("M48 40 L50 8 L72 22 Z", PAPER)
        + path("M112 40 L110 8 L88 22 Z", PAPER)
        + path("M52 30 L55 20 L62 25", stroke=SAKURA, width=3)
        + path("M108 30 L105 20 L98 25", stroke=SAKURA, width=3)
        + ellipse(80, 50, 36, 30, PAPER)
        + path("M50 78 Q80 92 110 78 L109 86 Q80 100 51 86 Z", VERMILION, INK, 4)
        + circle(80, 96, 7, GOLD, INK, 3.5)
        + ellipse(80, 112, 15, 11, GOLD, INK, 4)
        + path("M72 112 L88 112", stroke=INK, width=2.5)
    ),
}

# Per sprite: the face (see kit.face) and optional extra shapes per status.
POSES: dict[str, dict] = {
    "kokeshi": {
        "eyes": [(68, 46), (92, 46)], "mouth": (80, 58), "blush": [(60, 54), (100, 54)], "r": 5,
        "working": path("M30 70 Q24 80 30 90 M130 70 Q136 80 130 90", stroke=INK, width=2.5),
    },
    "daruma": {
        "eyes": [(67, 68), (93, 68)], "mouth": (80, 80), "blush": [(55, 78), (105, 78)],
        "working": path("M118 28 Q124 22 130 28", stroke=INK, width=2.5),
    },
    "chochin": {
        "eyes": [(69, 64), (91, 64)], "mouth": (80, 77), "blush": [(61, 74), (99, 74)], "r": 5,
        "working": path("M36 34 L28 28 M124 34 L132 28", stroke=GOLD, width=3),
    },
    "geta": {
        "eyes": [(65, 54), (95, 54)], "mouth": (80, 66), "blush": [(52, 64), (108, 64)],
        "working": path("M120 10 Q128 16 124 24", stroke=INK, width=2.5),
    },
    "sensu": {
        "eyes": [(67, 76), (93, 76)], "mouth": (80, 87), "blush": [(56, 86), (104, 86)],
        "working": path("M20 40 Q28 36 32 28 M140 40 Q132 36 128 28", stroke=INK, width=2.5),
    },
    "furin": {
        "eyes": [(67, 52), (93, 52)], "mouth": (80, 64), "blush": [(55, 62), (105, 62)],
        "working": path("M30 56 Q24 66 30 76 M130 56 Q136 66 130 76", stroke=INK, width=2.5),
    },
    "kendama": {
        "eyes": [(66, 74), (94, 74)], "mouth": (80, 86), "blush": [(52, 84), (108, 84)],
        "working": path("M104 14 Q112 22 106 30", stroke=INK, width=2.5),
    },
    "torii": {
        "eyes": [(68, 64), (92, 64)], "mouth": (80, 78), "blush": [(63, 74), (97, 74)], "r": 5,
        "working": path("M28 70 L22 64 M132 70 L138 64", stroke=INK, width=2.5),
    },
    "kasa": {
        "eyes": [(66, 58), (94, 58)], "mouth": (80, 69), "blush": [(52, 66), (108, 66)],
        "working": path("M24 30 L30 38 M136 30 L130 38", stroke=INK, width=2.5),
    },
    "maneki": {
        "eyes": [(66, 46), (94, 46)], "mouth": (80, 59), "blush": [(54, 56), (106, 56)],
        "working": path("M136 40 Q142 48 136 58 M142 36 Q150 48 142 62", stroke=INK, width=2.5),
    },
}
