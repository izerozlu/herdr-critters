"""Sprites batch B: nibbles, flutter, bramble, wiggle."""

import math

from .kit import cord, oval, piece, pose, qbez

_BRAMBLE_SPIKES = [
    (80 + (56 if i % 2 == 0 else 46) * math.cos(a), 92 + (48 if i % 2 == 0 else 38) * math.sin(a))
    for i, a in enumerate(math.pi + math.pi * k / 16 for k in range(17))
]

CRITTERS = {
    "nibbles": {  # a caterpillar
        "parts": [
            piece("#5e9a3a", ("ellipse", 30, 122, 5, 4), ("ellipse", 52, 123, 5, 4), ("ellipse", 76, 123, 5, 4), ("ellipse", 104, 123, 5, 4),
                  puff=1.5, seam=False),
            piece("#9fd36a", ("circle", 30, 106, 14)),
            piece("#8ec85a", ("circle", 52, 104, 16)),
            piece("#9fd36a", ("circle", 77, 101, 17)),
            cord("#5e9a3a", [(100, 56), (94, 38)], 3),
            cord("#5e9a3a", [(120, 56), (126, 38)], 3),
            piece("#f5c445", ("circle", 94, 37, 4.2), ("circle", 126, 37, 4.2), puff=2, seam=False),
            piece("#b8e07a", ("circle", 110, 82, 27)),
        ],
        "pose": pose([(100, 80), (120, 80)], (110, 92), [(92, 90), (128, 90)]),
    },
    "flutter": {  # a butterfly
        "parts": [
            piece("#f2a0bf", ("poly", oval(52, 72, 26, 21, -25))),
            piece("#f2a0bf", ("poly", oval(108, 72, 26, 21, 25))),
            piece("#f7c8d8", ("poly", oval(60, 104, 17, 15, 20))),
            piece("#f7c8d8", ("poly", oval(100, 104, 17, 15, -20))),
            piece("#f5c445", ("circle", 46, 70, 6.5), ("circle", 114, 70, 6.5), ("circle", 58, 106, 4.5), ("circle", 102, 106, 4.5), patch=True),
            piece("#5a3a32", ("ellipse", 80, 92, 10, 34)),
            cord("#5a3a32", [(73, 44), (64, 26)], 2.8),
            cord("#5a3a32", [(87, 44), (96, 26)], 2.8),
            piece("#5a3a32", ("circle", 63, 25, 4), ("circle", 97, 25, 4), puff=2, seam=False),
            piece("#f3dcc0", ("circle", 80, 56, 18)),
        ],
        "pose": pose([(73, 55), (87, 55)], (80, 64), [(68, 62), (92, 62)], r=3.9),
    },
    "bramble": {  # a hedgehog
        "parts": [
            piece("#5a3a26", ("ellipse", 58, 123, 10, 5), ("ellipse", 102, 123, 10, 5), puff=2, seam=False),
            piece("#8a5a3a", ("poly", _BRAMBLE_SPIKES + qbez((136, 92), (134, 118), (112, 121)) + qbez((48, 121), (26, 118), (24, 92))), seam=False),
            piece("#9a6a46", ("ellipse", 80, 98, 46, 26), seam=False),
            piece("#f1d9b0", ("ellipse", 80, 96, 32, 25)),
            piece("#3d3436", ("circle", 80, 99, 4), puff=1.5, seam=False),
        ],
        "pose": pose([(68, 89), (92, 89)], (80, 108), [(61, 101), (99, 101)], r=4.4),
    },
    "wiggle": {  # an earthworm with a sprout
        "parts": [
            piece("#5f8a46", ("poly", oval(100, 27, 8, 4, -30)), puff=2, seam=False),
            cord("#5f8a46", [(88, 42), (93, 29)], 2.4),
            piece("#ef9fb0", ("line", [(132, 118)] + qbez((132, 118), (56, 124), (56, 98)) + qbez((56, 98), (58, 78), (80, 66)), 20), seam=False),
            piece("#f4b3c0", ("circle", 86, 58, 19)),
        ],
        "pose": pose([(79, 57), (94, 57)], (86.5, 67), [(73, 66), (100, 66)], r=4.2),
    },
}
