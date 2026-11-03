"""Y2K theme art data: sprites, poses, pose marks, scenes and icons.

The engine (art/generate.py) reads these names from the package:
SPRITES, POSES, BATCHES, POSE_COLORS, BLOCKED_EYE, BANG, SWEAT, CHECK, BOLT, SCENES, ICONS.
A new batch file must be imported here and added to BATCHES, or it is not drawn.
"""

from . import batch_a, batch_b, batch_c
from .base import BANG, BLOCKED_EYE, BOLT, CHECK, POSE_COLORS, POSES, SPRITES, SWEAT
from .scenes import ICONS, SCENES

# The sprite batches, by name, each with its own SPRITES and POSES.
BATCHES = {"batch_a": batch_a, "batch_b": batch_b, "batch_c": batch_c}

for _name, _batch in BATCHES.items():
    assert not set(_batch.SPRITES) & set(SPRITES), f"{_name}: sprite name taken"
    assert set(_batch.SPRITES) == set(_batch.POSES), f"{_name}: SPRITES and POSES differ"
    SPRITES.update(_batch.SPRITES)
    POSES.update(_batch.POSES)

__all__ = ["BANG", "BATCHES", "BLOCKED_EYE", "BOLT", "CHECK", "ICONS", "POSES", "POSE_COLORS", "SCENES", "SPRITES", "SWEAT"]
