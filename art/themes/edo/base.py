"""Edo pose marks and colors shared by every sprite.

All sprites are 20 x 16, drawn standing on the scene's ground, with a dark ink
outline like a woodblock print. They live in batch_*.py, keyed by the agent
name they belong to (themes/edo/theme.js names).
"""

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {}
POSES: dict[str, dict] = {}

# Colors every pose may use on top of a sprite's own palette. Darker than
# retro's, so they read on the light paper scenes.
BLOCKED_EYE = "R"  # palette key for the eyes of a blocked critter
POSE_COLORS = {"R": "#c8302a", "X": "#c8302a", "q": "#3a6ea8", "E": "#4f7a2e", "U": "#d08a10"}

# Small marks placed in free space beside the sprite.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = [".U", "UU", "U."]
