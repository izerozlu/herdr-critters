"""Y2K pose marks and the shared sprite tables: 20 x 16 sprites, drawn standing on the scene's ground.

Every sprite is in a batch_*.py file, keyed by the agent name it belongs to
(themes/y2k/theme.js names). The scenes are bright, so each sprite has a dark outline.
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {}

# Colors every pose may use on top of a sprite's own palette. Darker than retro's,
# so the marks read on the bright scenes.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#ff2a6d", "X": "#e0115f", "q": "#1e7bff", "E": "#1f9e2c", "U": "#ffb000"}

# Small marks placed in free space beside the sprite.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = [".U", "UU", "U."]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {}
