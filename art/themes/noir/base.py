"""Noir base sprites and their poses: 20 x 16, drawn standing on the scene's ground.

Each is keyed by the agent name it belongs to (themes/noir/theme.js names).
Grays only, with blood red as the one accent. More sprites are in batch_*.py.
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {
    # An alley cat in a fedora and trench coat, a lit cigarette.
    "spade": (
        {"H": "#4a4a54", "h": "#7a7a84", "G": "#8c8c94", "g": "#b4b4ba", "W": "#e8e4d8", "k": "#16161a",
         "T": "#a49e90", "t": "#7a7468", "s": "#f0ece0", "r": "#d0303c"},
        [
            "....................",
            ".......HHHHHH.......",
            "......HHHHHHHH......",
            "......hhhhhhhh......",
            "...HHHHHHHHHHHHHH...",
            ".....GGGGGGGGGG.....",
            ".....GWWGGGGWWG.....",
            ".....GWkGGGGWkG.....",
            ".....GGGGkkGGGG.....",
            ".....gGGGGGGGGgsssr.",
            "....TTTggggggTTT....",
            "...TTTTtggggtTTTT...",
            "...TTTTTtTTtTTTTT...",
            "...tTTTTkkkkTTTTt...",
            "....TTTTTTTTTTTT....",
            "....kkk......kkk....",
        ],
    ),
    # A rat informant in a flat cap and a striped shirt.
    "bugsy": (
        {"C": "#5a5a64", "c": "#34343c", "f": "#6a6a72", "p": "#c4b4b4", "F": "#9a9aa0", "w": "#e8e4d8",
         "k": "#16161a", "n": "#2a2a2e", "V": "#4e4e58", "v": "#8a8a92"},
        [
            "....................",
            "........CCCCC.......",
            "..ff...CCCCCCC..ff..",
            ".fppfCCCCCCCCCCfppf.",
            "..fffccccccccccfff..",
            "....FFFFFFFFFFFF....",
            "....FwwFFFFFFwwF....",
            "....FwkFFFFFFkwF....",
            "....FFFFFFFFFFFF....",
            ".....FFFFFFFFFF.....",
            "......FFFFFFFF......",
            "......f.FnnF.f......",
            ".....VvVvVvVvV......",
            "....FVvVvVvVvVF...f.",
            ".....VvVvVvVvVffff..",
            ".....ff....ff.......",
        ],
    ),
    # A street pigeon in a newsboy cap.
    "louie": (
        {"c": "#3e3e46", "C": "#5e5e68", "B": "#8e9098", "b": "#5c5e66", "n": "#6a7a76", "w": "#e8e4d8",
         "k": "#16161a", "y": "#c8c4b8", "f": "#a08c8c"},
        [
            "....................",
            "......ccccc.........",
            ".....CCCCCCC........",
            "...ccccccccc........",
            ".....BBBBBB.........",
            "...yyBwBBBB.........",
            "....yBkBBBB.........",
            ".....BnnnnB.........",
            "....nnnnnnnB........",
            "...BBBBBBBBBBB......",
            "...BBBBBBBBBBBBB....",
            "...BBBBbbbbbbBBBB...",
            "....BBBbbbbbbBBBBBb.",
            ".....BBBBBBBBBB.bbb.",
            ".......ff..ff.......",
            "......fff.fff.......",
        ],
    ),
    # A crow in a pale fedora and a pinstripe suit, a red tie.
    "vito": (
        {"K": "#3a3a44", "k": "#6a6a76", "w": "#e8e4d8", "e": "#101014", "y": "#b0aca0", "H": "#d4d0c4",
         "h": "#1a1a1e", "S": "#4a4a54", "s": "#74747e", "W": "#e8e4d8", "r": "#c8283a"},
        [
            "....................",
            "......HHHHHHH.......",
            "......HHHHHHH.......",
            "......hhhhhhh.......",
            "...HHHHHHHHHHHHH....",
            ".....kKKKKKKKKk.....",
            ".....KwwKKKKwwK.....",
            ".....KweKKKKewK.....",
            ".....KKKKyyKKKK.....",
            "......KKKyyKKK......",
            ".....SSSWyyWSSS.....",
            "....SsSSWrrWSSsS....",
            "....SsSSSrrSSSsS....",
            "....SsSSSrrSSSsS....",
            "....SsSSSSSSSSsS....",
            ".....yy......yy.....",
        ],
    ),
}


# Colors every pose may use on top of a sprite's own palette.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#e0303c", "X": "#e0303c", "q": "#9aa4ae", "E": "#c8c6bc", "U": "#f4f1e8"}

# Small marks placed in free space beside the sprite. BOLT is a magnifier, CHECK
# the case-closed tick, SWEAT a drop of rain.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = ["UUU.", "U.U.", "UUU.", "...U"]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {
    "spade": {
        "face": "G", "line": "k", "eyes": [(6, 6), (7, 6), (12, 6), (13, 6)],
        "idle": [(18, 9, "t")],
        "working": [(18, 9, "U")],
        "blocked": [(15, 9, "...."), (9, 9, "kk")],
        "done": [(8, 9, "kGGk")],
    },
    "bugsy": {
        "face": "F", "line": "f", "eyes": [(5, 6), (6, 6), (13, 6), (14, 6)],
        "idle": [],
        "working": [(8, 10, "kk")],
        "blocked": [(9, 10, "kk")],
        "done": [(7, 10, "kFFFFk")],
    },
    "louie": {
        "face": "B", "line": "k", "eyes": [(6, 5)],
        "idle": [],
        "working": [(3, 6, "y")],
        "blocked": [(3, 6, "yk")],
        "done": [],
    },
    "vito": {
        "face": "K", "line": "k", "eyes": [(6, 6), (7, 6), (12, 6), (13, 6)],
        "idle": [],
        "working": [],
        "blocked": [(9, 9, "ee")],
        "done": [],
    },
}
