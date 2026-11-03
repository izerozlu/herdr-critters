"""Deepsea base sprites and their poses: 20 x 16, drawn resting on the scene's seabed.

Each is keyed by the agent name it belongs to (themes/deepsea/theme.js names).
More sprites are in batch_a.py.
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {
    # An anglerfish with a glowing lure over its big toothy mouth.
    "lumen": (
        {"B": "#6a56b8", "b": "#a894ec", "f": "#463a86", "e": "#eaffff", "m": "#1a0820", "w": "#ffffff", "L": "#7ffcff"},
        [
            "....................",
            "..........BBBBB.....",
            ".........B.....B....",
            ".........B....LLL...",
            "......BBBBBB..LLL...",
            "....BBBBBBBBBB.L....",
            "...BBBBBBBBeBBB.....",
            "f..BBBBBBBBeBBBB....",
            "ff.BBBBBBBBBBwmwm...",
            "fffBBBBBBBBBBmmmm...",
            "ff.BbbbbbbbBBwmwm...",
            "f..BBbbbbbbBBBBBB...",
            "....BBBBBBBBBBBB....",
            ".....BBBBBBBBBB.....",
            "......ff....ff......",
            ".....fff...fff......",
        ],
    ),
    # A jellyfish: a soft bell and trailing tentacles with glowing tips.
    "bloom": (
        {"P": "#e070d8", "p": "#ffb8f4", "k": "#2a0a3a", "T": "#b070ff", "t": "#7ffcff"},
        [
            "....................",
            "......PPPPPPPP......",
            ".....PppPPPPPPP.....",
            "....PpPPPPPPPPPP....",
            "....PPPPPPPPPPPP....",
            "....PPPkPPPPkPPP....",
            "....PPPkPPPPkPPP....",
            "....PPPPPPPPPPPP....",
            "...PPPPPPPPPPPPPP...",
            "...pPpPpPpPpPpPpP...",
            "....T..T.TT.T..T....",
            "....T.T..TT..T.T....",
            "...T..T..T.T.T..T...",
            "...T.T..T..T..T.T...",
            "....T...T..T...T....",
            "....t...t..t...t....",
        ],
    ),
    # An octopus with glowing spots, curling its arms on the sand.
    "inky": (
        {"O": "#d0488a", "o": "#ff90c4", "k": "#1a0820", "g": "#7ffcff"},
        [
            "....................",
            ".......OOOOOO.......",
            "......OooOOOOO......",
            ".....OoOOgOOgOO.....",
            ".....OOOOOOOOOO.....",
            ".....OOOOOOOOOO.....",
            ".....OOkOOOOkOO.....",
            ".....OOkOOOOkOO.....",
            ".....OOOOOOOOOO.....",
            "....OOOOOOOOOOOO....",
            "...OOOOOOOOOOOOOO...",
            "..OO.OO.OOOO.OO.OO..",
            "..O..O..O..O..O..O..",
            "..O..OO.O..O.OO..O..",
            "..OO..O.OO.OO.O.OO..",
            "...oo.oo......oo.oo.",
        ],
    ),
    # A squid: fins on top of a long mantle, eyes low, tentacles under.
    "kraken": (
        {"Q": "#36b4c8", "q": "#9ff4ff", "e": "#eaffff", "k": "#06202a", "r": "#ff6aa0"},
        [
            ".........QQ.........",
            "........QqQQ........",
            ".....QQQqQQQQQQ.....",
            "......QQqQQQQQ......",
            ".......QqQQQQ.......",
            ".......QQQQQQ.......",
            ".......QQQQQQ.......",
            "......QQQQQQQQ......",
            "......QeQQQQeQ......",
            "......QeQQQQeQ......",
            "......QQQQQQQQ......",
            ".....QQ.Q..Q.QQ.....",
            ".....Q..Q..Q..Q.....",
            "....Q...Q..Q...Q....",
            "....Q..Q....Q..Q....",
            "...qq..q....q..qq...",
        ],
    ),
    # A nautilus: a striped spiral shell, a hooded head and short tentacles.
    "coil": (
        {"C": "#f2e6d0", "s": "#d0703a", "d": "#8a4a2a", "H": "#e89a6a", "T": "#ffb88a", "k": "#1a1010"},
        [
            "....................",
            ".....CCCCCC.........",
            "...CCsCCCCsCC.......",
            "..CsCCCddCCCsC......",
            "..CsCCdCCdCCsCHHH...",
            ".CsCCdCddCdCCsHHHH..",
            ".CsCCdCdCCdCCsHkHH..",
            ".CsCCdCCddCCCsHkHH..",
            ".CsCCCdCCCCCsCHHHH..",
            "..CsCCCddddCsCHHHT..",
            "..CCsCCCCCCsCCHTTTT.",
            "...CCssCCssCCHTT.T..",
            ".....CCCCCCCHTT.T.T.",
            "......CCCCC.T.T.T...",
            "............T..T..T.",
            "...........T..T..T..",
        ],
    ),
    # A deep sea crab: big claws up, eyes on stalks.
    "pinch": (
        {"K": "#e8503a", "k": "#ff9a7a", "e": "#1a0808", "w": "#fff4ec"},
        [
            "....................",
            "..KK............KK..",
            ".K..K..........K..K.",
            ".KKKK..........KKKK.",
            "..KK...e....e...KK..",
            "..KK...e....e...KK..",
            "...KK..K....K..KK...",
            "....KKKKKKKKKKKK....",
            "...KKkkKKKKKKkkKK...",
            "...KKKKKKKKKKKKKK...",
            "...KKKKKKKKKKKKKK...",
            "....KKKKKKKKKKKK....",
            "...K.K.K....K.K.K...",
            "..K.K.K......K.K.K..",
            "..K.K..K....K..K.K..",
            ".K.K...K....K...K.K.",
        ],
    ),
}


# Colors every pose may use on top of a sprite's own palette.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#ff4f8b", "X": "#ff4f8b", "q": "#8fe4ff", "E": "#6bffb0", "U": "#3ff0ff"}

# Small marks placed in free space beside the sprite: an SOS bang, a rising bubble,
# a check and a sonar ping.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = [".q.", "q.q", ".q."]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = ["U.", ".U", ".U", "U."]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {
    "lumen": {
        "face": "B", "line": "b", "eyes": [(11, 6)],
        "idle": [(14, 3, "fff"), (14, 4, "fff"), (15, 5, "f")],
        "working": [(14, 2, "LLL")],
        "blocked": [(14, 3, "RRR"), (14, 4, "RRR"), (15, 5, "R")],
        "done": [(13, 8, "BBBB"), (13, 9, "wmwm"), (13, 10, "BBBB")],
    },
    "bloom": {
        "face": "P", "line": "k", "eyes": [(7, 5), (12, 5)],
        "idle": [(4, 15, "T"), (8, 15, "T"), (11, 15, "T"), (15, 15, "T")],
        "working": [(4, 15, "U"), (8, 15, "U"), (11, 15, "U"), (15, 15, "U")],
        "blocked": [(9, 7, "kk")],
        "done": [(5, 7, "p"), (14, 7, "p"), (8, 7, "k"), (11, 7, "k"), (9, 8, "kk")],
    },
    "inky": {
        "face": "O", "line": "k", "eyes": [(7, 6), (12, 6)],
        "idle": [(9, 3, "O"), (12, 3, "O")],
        "working": [(9, 3, "U"), (12, 3, "U")],
        "blocked": [(9, 8, "kk"), (9, 9, "kk")],
        "done": [(6, 8, "o"), (13, 8, "o"), (8, 8, "kOOk"), (9, 9, "kk")],
    },
    "kraken": {
        "face": "Q", "line": "k", "eyes": [(7, 8), (12, 8)],
        "idle": [],
        "working": [(9, 0, "UU")],
        "blocked": [(9, 10, "kk")],
        "done": [(8, 10, "rQQr")],
    },
    "coil": {
        "face": "H", "line": "k", "eyes": [(15, 6)],
        "idle": [],
        "working": [(19, 10, "U"), (18, 12, "U")],
        "blocked": [(17, 8, "k")],
        "done": [(16, 8, "kk")],
    },
    "pinch": {
        "face": "K", "line": "e", "eyes": [(7, 4), (12, 4)],
        "idle": [],
        "working": [(2, 1, "UU"), (16, 1, "UU")],
        "blocked": [(8, 9, "eeee")],
        "done": [(8, 9, "eKKe"), (9, 10, "ee")],
    },
}
