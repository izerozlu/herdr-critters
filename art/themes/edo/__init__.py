"""Edo theme art: vector woodblock sprites, scenes and icons.

A vector theme for the engine (art/generate.py): VECTOR, SPRITES, BATCHES, SCENES, ICONS.
Each batch file has SPRITES (name -> body SVG) and POSES (name -> face and per-status
extras, see kit.face). A new batch file must be imported here and added to BATCHES.
"""

from functools import partial

from . import batch_a, batch_b, batch_c
from .kit import sprite
from .scenes import ICONS, SCENES

VECTOR = True
BATCHES = {"batch_a": batch_a, "batch_b": batch_b, "batch_c": batch_c}
SPRITES = {}

for _name, _batch in BATCHES.items():
    assert not set(_batch.SPRITES) & set(SPRITES), f"{_name}: sprite name taken"
    assert set(_batch.SPRITES) == set(_batch.POSES), f"{_name}: SPRITES and POSES differ"
    for _sprite, _body in _batch.SPRITES.items():
        _batch.SPRITES[_sprite] = SPRITES[_sprite] = partial(sprite, _body, _batch.POSES[_sprite])

__all__ = ["BATCHES", "ICONS", "SCENES", "SPRITES", "VECTOR"]
