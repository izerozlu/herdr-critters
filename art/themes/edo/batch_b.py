"""Sprites batch B: tempura, wasabi, sake, udon, natto, yuzu, miso, senbei, anpan, tamago."""

from .kit import INK, PAPER, circle, ellipse, path, rect

NORI = "#26302a"
BATTER = "#e6bf72"
VERMILION = "#c23b22"
INDIGO = "#2d4a7a"
MATCHA = "#8fb050"
YUZU = "#f0c43a"
STEAM = "#c9c2b0"

# Per sprite: the body, drawn back to front.
SPRITES: dict[str, str] = {
    "tempura": (
        path("M80 44 Q44 22 56 4 Q68 8 80 22 Q92 8 104 4 Q116 22 80 44 Z", VERMILION)
        + path("M80 44 L80 24", stroke=INK, width=2.5)
        + path("M80 36 Q124 34 122 78 Q122 122 80 122 Q38 122 38 78 Q36 34 80 36 Z", BATTER)
        + path("M44 100 L36 108 M116 100 L124 108", stroke=INK, width=3)
        + path("M52 52 Q58 40 70 38", stroke=PAPER, width=4)
        + path("M56 108 Q66 114 78 112", stroke="#c39a4c", width=3)
    ),
    "wasabi": (
        path("M80 40 Q60 26 48 8 Q70 6 80 24 Q90 6 112 8 Q100 26 80 40 Z", MATCHA)
        + path("M80 40 L80 14", stroke=INK, width=2.5)
        + path("M80 36 Q124 36 120 76 Q114 108 90 120 Q80 124 70 120 Q46 108 40 76 Q36 36 80 36 Z", "#b4cf78")
        + path("M52 58 Q58 46 70 44", stroke=PAPER, width=4)
        + path("M62 108 L72 108 M92 108 L100 108", stroke="#7a9a40", width=3)
    ),
    "sake": (
        path("M70 12 L90 12 L90 40 Q116 52 116 84 L116 114 Q116 122 108 122 L52 122 Q44 122 44 114 L44 84 Q44 52 70 40 Z", PAPER)
        + path("M44 100 L116 100 L116 114 Q116 122 108 122 L52 122 Q44 122 44 114 Z", INDIGO)
        + path("M70 12 L90 12 L90 40 Q80 44 70 40 Z", PAPER)
        + path("M66 22 L94 22", stroke=INDIGO, width=4)
        + path("M44 100 L116 100", stroke=INK, width=3)
    ),
    "udon": (
        ellipse(80, 66, 44, 36, PAPER)
        + path("M52 52 Q80 38 108 52 M46 66 Q80 50 114 66", stroke="#d8d0bc", width=3)
        + circle(104, 44, 12, PAPER)
        + path("M104 44 Q108 38 112 44 Q108 52 100 48", stroke="#e8a0b0", width=3.5)
        + circle(104, 44, 5, "#e8a0b0", None)
        + path("M34 84 L126 84 Q124 122 104 122 L56 122 Q36 122 34 84 Z", VERMILION)
        + path("M40 92 Q80 100 120 92", stroke="#e2735a", width=3)
    ),
    "natto": (
        path("M60 36 Q56 20 66 12 M82 34 Q88 18 78 8 M100 38 Q112 24 106 14", stroke=PAPER, width=5)
        + path("M60 36 Q56 20 66 12 M82 34 Q88 18 78 8 M100 38 Q112 24 106 14", stroke="#d8d0bc", width=2)
        + path("M40 84 Q40 40 80 40 Q120 40 120 84 Z", "#c8a066")
        + ellipse(50, 74, 5, 3.5, "#8a6234", None) + ellipse(110, 74, 5, 3.5, "#8a6234", None) + ellipse(80, 48, 5, 3.5, "#8a6234", None)
        + path("M44 82 L116 82 Q114 122 96 122 L64 122 Q46 122 44 82 Z", "#6a5a8a")
        + path("M50 94 Q80 102 110 94", stroke="#9a8aba", width=3)
    ),
    "yuzu": (
        path("M80 40 Q72 22 50 22 Q56 40 80 40 Z", MATCHA)
        + path("M80 40 L62 28", stroke=INK, width=2.5)
        + path("M80 36 Q92 36 100 42 Q116 46 120 62 Q126 80 118 98 Q108 122 80 122 Q52 122 42 98 Q34 80 40 62 Q44 46 60 42 Q68 36 80 36 Z", YUZU)
        + path("M52 56 Q58 46 68 44", stroke=PAPER, width=4)
        + path("M104 104 Q94 114 82 114", stroke="#c89a1a", width=3)
    ),
    "miso": (
        path("M96 8 Q86 20 96 30 M72 10 Q62 22 72 32", stroke=STEAM, width=4)
        + path("M36 54 L124 54 Q124 122 100 122 L60 122 Q36 122 36 54 Z", "#2b2430")
        + ellipse(80, 54, 44, 14, "#c89a3a")
        + rect(62, 46, 12, 12, PAPER, 2, INK, 3)
        + rect(88, 50, 12, 12, PAPER, 2, INK, 3)
        + circle(110, 52, 4, MATCHA, INK, 2.5)
        + circle(50, 54, 4, MATCHA, INK, 2.5)
        + path("M40 108 Q80 118 120 108", stroke=VERMILION, width=4)
    ),
    "senbei": (
        circle(80, 80, 44, "#d9a85a")
        + path("M50 58 Q56 46 68 42", stroke=PAPER, width=4)
        + "".join(ellipse(x, y, 3, 2, "#a8742e", None) for x, y in ((100, 46), (110, 64), (52, 84)))
        + path("M39 96 L121 96 A44 44 0 0 1 108 114 L52 114 A44 44 0 0 1 39 96 Z", NORI)
        + path("M46 105 L114 105", stroke="#3c4a40", width=2.5)
        + circle(80, 80, 44, "none")
    ),
    "anpan": (
        path("M36 106 Q34 50 80 44 Q126 50 124 106 Q124 122 108 122 L52 122 Q36 122 36 106 Z", "#d4a064")
        + path("M50 66 Q56 54 68 50", stroke=PAPER, width=4)
        + ellipse(80, 48, 11, 6, "#f0d6a0")
        + "".join(ellipse(x, y, 2.4, 1.4, INK, None) for x, y in ((76, 48), (84, 47), (80, 51)))
    ),
    "tamago": (
        rect(36, 86, 88, 36, PAPER, 12)
        + rect(42, 32, 76, 62, "#f2c84a", 12)
        + path("M52 46 Q80 40 108 46", stroke="#d9a62a", width=3)
        + rect(40, 84, 80, 16, NORI, 3)
        + path("M46 92 L114 92", stroke="#3c4a40", width=2.5)
    ),
}

# Per sprite: the face (see kit.face) and optional extra shapes per status.
POSES: dict[str, dict] = {
    "tempura": {
        "eyes": [(66, 70), (94, 70)], "mouth": (80, 86), "blush": [(54, 84), (106, 84)],
        "working": path("M122 40 Q128 34 122 28", stroke=STEAM, width=3),
    },
    "wasabi": {
        "eyes": [(66, 68), (94, 68)], "mouth": (80, 84), "blush": [(54, 82), (106, 82)],
    },
    "sake": {
        "eyes": [(66, 70), (94, 70)], "mouth": (80, 84), "blush": [(54, 82), (106, 82)],
    },
    "udon": {
        "eyes": [(64, 62), (92, 62)], "mouth": (78, 76), "blush": [(52, 74), (104, 74)],
        "working": path("M60 30 Q52 20 60 10 M80 28 Q72 18 80 8", stroke=STEAM, width=4),
    },
    "natto": {
        "eyes": [(66, 62), (94, 62)], "mouth": (80, 74), "blush": [(54, 72), (106, 72)],
    },
    "yuzu": {
        "eyes": [(66, 76), (94, 76)], "mouth": (80, 92), "blush": [(54, 90), (106, 90)],
    },
    "miso": {
        "eyes": [(64, 88), (96, 88)], "mouth": (80, 100), "blush": [(52, 98), (108, 98)], "ink": PAPER,
        "working": path("M50 40 Q42 30 50 20 M110 40 Q102 30 110 20", stroke=STEAM, width=4),
    },
    "senbei": {
        "eyes": [(66, 66), (94, 66)], "mouth": (80, 80), "blush": [(54, 78), (106, 78)],
    },
    "anpan": {
        "eyes": [(66, 82), (94, 82)], "mouth": (80, 96), "blush": [(54, 94), (106, 94)],
    },
    "tamago": {
        "eyes": [(66, 62), (94, 62)], "mouth": (80, 74), "blush": [(54, 72), (106, 72)],
    },
}
