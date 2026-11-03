"""Deepsea theme art: soft gel sea critters, scenes and icons, drawn with skia-python by kit.py.

A raster theme for the engine (art/generate.py): RASTER, SPRITES, BATCHES, SCENES, ICONS.
Each batch file has CRITTERS (name -> Critter); this module turns each into SPRITES
(name -> a function of the status that gives PNG bytes). A new batch file must be
imported here and added to BATCHES.
"""

from functools import partial

from . import batch_a, batch_b
from .kit import sprite
from .scenes import ICONS, SCENES

RASTER = True
BATCHES = {"batch_a": batch_a, "batch_b": batch_b}
SPRITES = {}

for _name, _batch in BATCHES.items():
    assert not set(_batch.CRITTERS) & set(SPRITES), f"{_name}: critter name taken"
    _batch.SPRITES = {_critter: partial(sprite, _c) for _critter, _c in _batch.CRITTERS.items()}
    SPRITES.update(_batch.SPRITES)

__all__ = ["BATCHES", "ICONS", "RASTER", "SCENES", "SPRITES"]
