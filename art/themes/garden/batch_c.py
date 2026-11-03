"""Sprites batch C: clover, digby, hazel, poppy."""

from .kit import cord, piece, pose, qbez

DARK = "#2f4438"
_CLOVER_SHELL = ("ellipse", 80, 94, 45, 31)

CRITTERS = {
    "clover": {  # a green beetle with a clover leaf on its back
        "parts": [
            cord(DARK, [(52, 100), (36, 108), (32, 124)], 3.6),
            cord(DARK, [(108, 100), (124, 108), (128, 124)], 3.6),
            cord(DARK, [(66, 116), (60, 127)], 3.6),
            cord(DARK, [(94, 116), (100, 127)], 3.6),
            cord(DARK, [(72, 42), (60, 26)], 3.2),
            cord(DARK, [(88, 42), (100, 26)], 3.2),
            piece(DARK, ("circle", 59, 25, 4), ("circle", 101, 25, 4), puff=2, seam=False),
            piece("#4fae8a", _CLOVER_SHELL),
            cord(DARK, [(80, 68), (80, 124)], 2.4),
            piece("#b4e08e", ("circle", 62, 98, 6), ("circle", 74, 98, 6), ("circle", 68, 89, 6), patch=True),
            piece("#b4e08e", ("circle", 98, 108, 4.5), ("circle", 107, 108, 4.5), ("circle", 102.5, 101, 4.5), patch=True),
            piece(DARK, ("ellipse", 80, 56, 26, 21)),
        ],
        "pose": pose([(70, 54), (90, 54)], (80, 66), [(62, 64), (98, 64)], light=True),
    },
    "digby": {  # a mole
        "parts": [
            piece("#f2a8b0", ("ellipse", 64, 124, 9, 4), ("ellipse", 96, 124, 9, 4), puff=1.5, seam=False),
            piece("#7d7480", ("ellipse", 80, 88, 38, 38)),
            piece("#958c98", ("ellipse", 80, 106, 22, 15), seam=False),
            piece("#f2a8b0", ("ellipse", 41, 98, 12, 9), ("ellipse", 119, 98, 12, 9)),
            piece("#f2a8b0", ("circle", 80, 82, 5.5), puff=2, seam=False),
        ],
        "pose": pose([(67, 72), (93, 72)], (80, 93), [(60, 84), (100, 84)], r=4.0),
    },
    "hazel": {  # a field mouse
        "parts": [
            cord("#e8909e", qbez((110, 118), (140, 120), (138, 96)), 2.8),
            piece("#e8909e", ("ellipse", 66, 124, 8, 4), ("ellipse", 94, 124, 8, 4), puff=1.5, seam=False),
            piece("#d9a86e", ("circle", 52, 46, 14), ("circle", 108, 46, 14)),
            piece("#f2b0b8", ("circle", 52, 47, 7.5), ("circle", 108, 47, 7.5), patch=True),
            piece("#d9a86e", ("ellipse", 80, 96, 36, 30)),
            piece("#d9a86e", ("ellipse", 80, 70, 31, 24)),
            piece("#f6e2bc", ("ellipse", 80, 106, 20, 16)),
            piece("#e8909e", ("circle", 80, 77, 3.4), puff=1.5, seam=False),
        ],
        "pose": pose([(69, 67), (91, 67)], (80, 84), [(61, 77), (99, 77)], r=4.2),
    },
    "poppy": {  # a robin
        "parts": [
            cord("#e88a3a", [(70, 116), (68, 127)], 2.8),
            cord("#e88a3a", [(90, 116), (92, 127)], 2.8),
            piece("#7a4e30", ("poly", [(108, 100), (138, 84), (136, 104), (114, 114)])),
            piece("#8a5a3a", ("poly", [(74, 54), (70, 44), (80, 50), (84, 42), (86, 54)]), puff=2, seam=False),
            piece("#8a5a3a", ("ellipse", 80, 88, 37, 35)),
            piece("#f08a3a", ("ellipse", 80, 100, 25, 20)),
            piece("#f5c445", ("poly", [(73, 78), (87, 78), (80, 88)]), puff=1.5, seam=False),
        ],
        "pose": pose([(69, 72), (91, 72)], None, [(62, 82), (98, 82)], r=4.4),
    },
}
