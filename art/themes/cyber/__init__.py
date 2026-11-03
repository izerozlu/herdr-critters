"""Cyber theme art: flat vector mascots with holo chrome, drawn in code.

A vector theme for the engine (art/generate.py): VECTOR, SPRITES, BATCHES, SCENES, ICONS.
Each batch file has SPRITES (name -> draw(status), the sprite's SVG body); the shared
look is in kit.py, scenes and icons in scenes.py. A new batch file must be imported
here and added to BATCHES.
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
    for _sprite, _draw in _batch.SPRITES.items():
        _batch.SPRITES[_sprite] = SPRITES[_sprite] = partial(sprite, _draw)

__all__ = ["BATCHES", "ICONS", "SCENES", "SPRITES", "VECTOR"]
