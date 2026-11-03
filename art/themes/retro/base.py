"""Retro base sprites and their poses: 20 x 16, drawn standing on the scene's ground.

Each is keyed by the agent name it belongs to (themes/retro/theme.js names).
More sprites are in batch_*.py.
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {
    "byte": (
        {"r": "#e0483e", "G": "#5b6472", "L": "#c9d1dc", "c": "#5ee6f2", "d": "#3a404a", "D": "#2b3038", "b": "#e0483e"},
        [
            ".........r..........",
            ".........G..........",
            ".....GGGGGGGGGG.....",
            "....GLLLLLLLLLLG....",
            "....GLccLLLLccLG....",
            "....GLccLLLLccLG....",
            "....GLLLLLLLLLLG....",
            "....GLLLddddLLLG....",
            "....GGGGGGGGGGGG....",
            "......DDDDDDDD......",
            ".....GLLLLLLLLG.....",
            "...GGGLbLLLLcLGGG...",
            "...G.GLLLLLLLLG.G...",
            ".....GGGGGGGGGG.....",
            "......DD....DD......",
            ".....DDD....DDD.....",
        ],
    ),
    "pixel": (
        {"B": "#e8d9b0", "b": "#b8a67c", "S": "#1b2a3a", "c": "#5ee6f2", "r": "#e0483e", "D": "#6e6250"},
        [
            "....................",
            "...BBBBBBBBBBBBBB...",
            "...BSSSSSSSSSSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BSSScSSSScSSSB...",
            "...BSSScSSSScSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BSScSSSSSSScSB...",
            "...BSSSccccccSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BBBBBBBBBBBBBB...",
            "...BrbBBBBBBBBbbB...",
            "...bbbbbbbbbbbbbb...",
            ".......DDDDDD.......",
            ".....bbbbbbbbbb.....",
            ".....DDDDDDDDDD.....",
        ],
    ),
    "quill": (
        {"Y": "#f7c83a", "y": "#d89a1c", "H": "#7a5a2c", "h": "#a07a3c", "k": "#1a1a1a", "o": "#f08a24", "w": "#fff4c8"},
        [
            "......HHHHH.........",
            ".....HhhhhhH........",
            "....HhhhhhhhH.......",
            "....HYYYYYYYH.......",
            "....YYwkYYYYY.......",
            "....YYkkYYYYYoo.....",
            "....YYYYYYYYYooo....",
            ".....YYYYYYYY.......",
            "......YYYY..........",
            "...YYYYYYYYYYY......",
            "..YYYYYYYYYYYYY..Y..",
            "..YYYyyyyyYYYYYYYY..",
            "..YYYYyyyyYYYYYYY...",
            "...YYYYYYYYYYYYY....",
            ".....oo....oo.......",
            "....ooo...ooo.......",
        ],
    ),
    "miso": (
        {"K": "#d9944a", "k": "#f4dcb0", "s": "#8a4e22", "g": "#2f7a2a", "p": "#f29bb6", "w": "#fff0d8"},
        [
            "....................",
            "....K........K......",
            "....KK......KK......",
            "....KpK....KpK......",
            "....KKKsKKsKKK......",
            "...KKKKsKKsKKKK.....",
            "...KKgKKKKKKgKK.....",
            "...KKgKKKKKKgKK.....",
            "...wKKKKppKKKKw.....",
            "....KKKKKKKKKK......",
            "....KsKKKKKKKsK..s..",
            "...KKKkkkkkkKKK..K..",
            "...KKKkkkkkkKKKKsK..",
            "...KKKKKKKKKKKKKK...",
            "...KK.KK..KK.KK.....",
            "...ww.ww..ww.ww.....",
        ],
    ),
    "umbra": (
        {"W": "#e9e6ff", "w": "#b9b2e8", "k": "#2a2440", "p": "#f29bb6"},
        [
            "....................",
            "......WWWWWWW.......",
            ".....WWWWWWWWW......",
            "....WWWWWWWWWWW.....",
            "....WWkkWWWkkWW.....",
            "....WWkkWWWkkWW.....",
            "....WpWWWWWWWpW.....",
            "....WWWWkkkWWWW.....",
            "....WWWWWWWWWWW.....",
            "....WWWWWWWWWWW.....",
            "....WwWWWWWWWwW.....",
            "....WwwWWWWWwwW.....",
            "....WWWWWWWWWWW.....",
            "....WWW.WWW.WWW.....",
            "....WW...W...WW.....",
            "....................",
        ],
    ),
}


# Colors every pose may use on top of a sprite's own palette.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#ff5a5a", "X": "#ff5a5a", "q": "#6ec8ff", "E": "#9be36a", "U": "#fff27a"}

# Small marks placed in free space beside the sprite.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = [".U", "UU", "U."]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {
    "byte": {
        "face": "L", "line": "d", "eyes": [(6, 4), (7, 4), (12, 4), (13, 4)],
        "idle": [(9, 0, "d")],
        "working": [(9, 0, "U"), (7, 11, "U"), (12, 11, "E")],
        "blocked": [(7, 7, "dLdLd")],
        "done": [(7, 6, "d"), (12, 6, "d")],
    },
    "pixel": {
        "face": "S", "line": "c", "eyes": [(7, 4), (12, 4)],
        "idle": [(6, 7, "S"), (13, 7, "S"), (7, 8, "S"), (12, 8, "S"), (4, 11, "D")],
        "working": [(4, 11, "E")],
        "blocked": [(6, 7, "S"), (13, 7, "S"), (6, 9, "c"), (13, 9, "c")],
        "done": [],
    },
    "quill": {
        "face": "Y", "line": "k", "eyes": [(6, 4), (7, 4)],
        "idle": [],
        "working": [(8, 1, "U")],
        "blocked": [],
        "done": [],
    },
    "miso": {
        "face": "K", "line": "s", "eyes": [(5, 6), (12, 6)],
        "idle": [(5, 3, "s"), (12, 3, "s")],
        "working": [(5, 3, "U"), (12, 3, "U")],
        "blocked": [(8, 8, "ss"), (8, 9, "ss")],
        "done": [(4, 8, "p"), (13, 8, "p"), (7, 9, "sKKs")],
    },
    "umbra": {
        "face": "W", "line": "k", "eyes": [(6, 4), (7, 4), (11, 4), (12, 4)],
        "idle": [(8, 7, "WkW")],
        "working": [],
        "blocked": [(8, 8, "kkk")],
        "done": [(7, 7, "kWWWk"), (8, 8, "kkk")],
    },
}
