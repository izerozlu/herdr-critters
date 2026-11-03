"""Garden base sprites and their poses: 20 x 16, drawn standing on the scene's ground.

Each is keyed by the agent name it belongs to (themes/garden/theme.js names).
Every sprite has a dark brown outline so it reads on the light scenes.
More sprites are in batch_*.py.
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {
    "dotty": (
        {"o": "#4a3526", "h": "#3a3236", "w": "#ffffff", "r": "#e2483e", "k": "#2a1e16", "p": "#f29bb6"},
        [
            "....................",
            "......o......o......",
            ".......o....o.......",
            ".....oooooooooo.....",
            "....ohhhhhhhhhho....",
            "....ohhwhhhhwhho....",
            "....ohhwhhhhwhho....",
            "...oohhhhhhhhhhoo...",
            "..orrrrrrkkrrrrrro..",
            ".orrkkrrrkkrrrkkrro.",
            ".orrkkrrrkkrrrkkrro.",
            ".orrrrrrrkkrrrrrrro.",
            ".orrrkkrrkkrrkkrrro.",
            "..orrkkrrkkrrkkrro..",
            "...oorrrrkkrrrroo...",
            "....oo.oo..oo.oo....",
        ],
    ),
    "buzz": (
        {"o": "#4a3526", "w": "#e6f4ff", "y": "#ffcf3a", "k": "#2a1e16", "p": "#f29bb6"},
        [
            "......oo....oo......",
            ".....owwo..owwo.....",
            ".....owwwooowwo.....",
            "......oooooooo......",
            ".....oyyyyyyyyo.....",
            "....oyykyyyykyyo....",
            "....oyykyyyykyyo....",
            "....oyyyyyyyyyyo....",
            "....okkkkkkkkkko....",
            "....oyyyyyyyyyyo....",
            "....okkkkkkkkkko....",
            "....oyyyyyyyyyyo....",
            ".....okkkkkkkko.....",
            "......oyyyyyyo......",
            ".......oooooo.......",
            ".........oo.........",
        ],
    ),
    "shelly": (
        {"o": "#4a3526", "b": "#ead2a8", "s": "#e8a060", "S": "#a8603a", "k": "#2a1e16", "p": "#f29bb6"},
        [
            "....................",
            "..o..o..............",
            "..o..o.....ooooo....",
            "..o..o...oosssssoo..",
            ".oooooo.ossSSSSSsso.",
            "obbbbbbo.osSsssssSso",
            "obkbbkbo.osSsSSSsSso",
            "obkbbkbo.osSsSsSsSso",
            "obbbbbbo.osSsSSssSso",
            "obbbbbbo.osSsssssSso",
            "obbbbbbo.ossSSSSSsso",
            "obbbbbbo..oosssssoo.",
            "obbbbbbbooooooooooo.",
            "obbbbbbbbbbbbbbbbbbo",
            "obbbbbbbbbbbbbbbbbbo",
            ".oooooooooooooooooo.",
        ],
    ),
    "ribbit": (
        {"o": "#4a3526", "w": "#ffffff", "k": "#2a1e16", "g": "#7cc35a", "G": "#3f7a30", "l": "#e8f0b0", "p": "#f29bb6"},
        [
            "....................",
            "...oooo......oooo...",
            "..owwwwo....owwwwo..",
            "..owkkwo....owkkwo..",
            "..owkkwoooooowkkwo..",
            "..oggggggggggggggo..",
            ".oggggggggggggggggo.",
            ".oggggggggggggggggo.",
            ".ogggGGGGGGGGGGgggo.",
            ".oggggggggggggggggo.",
            "..ogggllllllllgggo..",
            ".oggggllllllllggggo.",
            ".oggggllllllllggggo.",
            "ogggggllllllllgggggo",
            "ogggggoooooooogggggo",
            "oooooo........oooooo",
        ],
    ),
}


# Colors every pose may use on top of a sprite's own palette.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#d0342c", "X": "#d0342c", "q": "#3a8fd0", "E": "#3d8b37", "U": "#e09a00"}

# Small marks placed in free space beside the sprite.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
# Working: a little sun sparkle instead of retro's bolt.
BOLT = [".U.", "UUU", ".U."]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {
    "dotty": {
        "face": "h", "line": "w", "eyes": [(7, 5), (12, 5)],
        "idle": [],
        "working": [(6, 1, "U"), (13, 1, "U")],
        "blocked": [(9, 7, "w")],
        "done": [(6, 7, "p"), (13, 7, "p"), (9, 7, "ww")],
    },
    "buzz": {
        "face": "y", "line": "k", "eyes": [(7, 5), (12, 5)],
        "idle": [],
        "working": [],
        "blocked": [(9, 7, "k")],
        "done": [(5, 7, "p"), (14, 7, "p"), (9, 7, "kk")],
    },
    "shelly": {
        "face": "b", "line": "k", "eyes": [(2, 6), (5, 6)],
        "idle": [],
        "working": [(2, 1, "U"), (5, 1, "U")],
        "blocked": [(3, 9, "k")],
        "done": [(1, 8, "p"), (6, 8, "p"), (3, 9, "kk")],
    },
    "ribbit": {
        "face": "w", "line": "G", "eyes": [(4, 3), (5, 3), (14, 3), (15, 3)],
        "idle": [(5, 8, "gGGGGGGGGg")],
        "working": [],
        "blocked": [(5, 8, "GgGgGgGgGg")],
        "done": [(5, 7, "G"), (14, 7, "G"), (5, 8, "g"), (14, 8, "g"), (3, 7, "p"), (16, 7, "p")],
    },
}
