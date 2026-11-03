"""Sprites batch A: dotty, buzz, shelly, ribbit."""

from .kit import cord, oval, piece, pose, qbez, spiral

DARK = "#3d3436"
_DOTTY_SHELL = ("ellipse", 80, 94, 46, 31)
_BUZZ_BODY = ("ellipse", 80, 84, 37, 38)

CRITTERS = {
    "dotty": {  # a ladybug
        "parts": [
            cord(DARK, [(58, 112), (48, 127)], 4.5),
            cord(DARK, [(102, 112), (112, 127)], 4.5),
            cord(DARK, [(72, 42), (62, 24)], 3.2),
            cord(DARK, [(88, 42), (98, 24)], 3.2),
            piece(DARK, ("circle", 61, 23, 4.2), ("circle", 99, 23, 4.2), puff=2, seam=False),
            piece("#e0574e", _DOTTY_SHELL),
            piece(DARK, ("circle", 58, 86, 7.5), ("circle", 102, 86, 7.5), ("circle", 54, 108, 6), ("circle", 106, 108, 6),
                  ("circle", 70, 116, 5), ("circle", 90, 116, 5), clip=[_DOTTY_SHELL], patch=True),
            cord(DARK, [(80, 70), (80, 124)], 2.4),
            piece(DARK, ("ellipse", 80, 56, 26, 21)),
        ],
        "pose": pose([(70, 54), (90, 54)], (80, 66), [(62, 64), (98, 64)], light=True),
    },
    "buzz": {  # a bumblebee
        "parts": [
            piece("#d8ecef", ("poly", oval(54, 46, 21, 14, -30))),
            piece("#d8ecef", ("poly", oval(106, 46, 21, 14, 30))),
            cord("#7a4e30", [(70, 50), (60, 30)], 3),
            cord("#7a4e30", [(90, 50), (100, 30)], 3),
            piece("#7a4e30", ("circle", 59, 29, 4), ("circle", 101, 29, 4), ("ellipse", 66, 123, 7, 4), ("ellipse", 94, 123, 7, 4), puff=2, seam=False),
            piece("#f5c445", _BUZZ_BODY),
            piece("#7a4e30", ("rect", 30, 95, 130, 104), ("rect", 30, 110, 130, 119), clip=[_BUZZ_BODY], patch=True),
        ],
        "pose": pose([(68, 72), (92, 72)], (80, 84), [(59, 82), (101, 82)], r=4.8),
    },
    "shelly": {  # a snail
        "parts": [
            piece("#efd3a0", ("poly", [(18, 126)] + qbez((18, 126), (24, 108), (60, 110)) + [(126, 108), (134, 126)]), seam=False),
            cord("#efd3a0", [(110, 56), (103, 37)], 3.2),
            cord("#efd3a0", [(122, 56), (127, 37)], 3.2),
            piece("#efd3a0", ("circle", 103, 36, 4.4), ("circle", 127, 36, 4.4), puff=2, seam=False),
            piece("#d98448", ("circle", 66, 80, 35)),
            cord("#8a4824", spiral(68, 82, 2, 27, 2.2, start=3.6), 2.6),
            piece("#efd3a0", ("ellipse", 116, 86, 18, 34)),
        ],
        "pose": pose([(110, 72), (123, 72)], (116.5, 84), [(104, 82), (129, 82)], r=4.2),
    },
    "ribbit": {  # a frog
        "parts": [
            piece("#6fae4a", ("ellipse", 42, 123, 15, 5), ("ellipse", 118, 123, 15, 5), puff=2, seam=False),
            piece("#8cc85a", ("circle", 56, 62, 15), ("circle", 104, 62, 15)),
            piece("#8cc85a", ("ellipse", 80, 96, 52, 30)),
            piece("#e2efb4", ("ellipse", 80, 106, 32, 16)),
            piece("#fbf3e2", ("circle", 56, 62, 9), ("circle", 104, 62, 9), puff=2, seam=False),
        ],
        "pose": pose([(56, 62), (104, 62)], (80, 86), [(48, 84), (112, 84)], r=5.6),
    },
}
