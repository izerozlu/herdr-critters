"""Noir theme art: raster silhouette sprites, scenes and icons, drawn with skia-python.

A raster theme for the engine (art/generate.py): RASTER, SPRITES, BATCHES, SCENES, ICONS,
each picture as PNG bytes. Each batch file has SPRITES (name -> kit.Critter); the kit
draws a critter in each status. A new batch file must be imported here and added to BATCHES.
"""

from functools import partial

from . import batch_a, batch_b, batch_c, batch_d
from .kit import sprite
from .scenes import ICONS, SCENES

RASTER = True
BATCHES = {"batch_a": batch_a, "batch_b": batch_b, "batch_c": batch_c, "batch_d": batch_d}
SPRITES = {}

for _name, _batch in BATCHES.items():
    assert not set(_batch.SPRITES) & set(SPRITES), f"{_name}: sprite name taken"
    for _sprite, _critter in _batch.SPRITES.items():
        SPRITES[_sprite] = partial(sprite, _critter)

__all__ = ["BATCHES", "ICONS", "RASTER", "SCENES", "SPRITES"]
