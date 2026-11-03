"""Garden theme art: felt craft critters, scenes and icons, drawn as PNG by kit.py.

A raster theme for the engine (art/generate.py): RASTER, SPRITES, BATCHES, SCENES, ICONS.
Each batch file has CRITTERS (name -> felt pieces and a face pose); this module turns each
into SPRITES (name -> a function of the status that gives PNG bytes). A new batch file
must be imported here and added to BATCHES.
"""

from functools import partial

from . import batch_a, batch_b, batch_c
from .kit import sprite
from .scenes import ICONS, SCENES

RASTER = True
BATCHES = {"batch_a": batch_a, "batch_b": batch_b, "batch_c": batch_c}
SPRITES = {}

for _name, _batch in BATCHES.items():
    assert not set(_batch.CRITTERS) & set(SPRITES), f"{_name}: critter name taken"
    _batch.SPRITES = {_critter: partial(sprite, _critter, _c) for _critter, _c in _batch.CRITTERS.items()}
    SPRITES.update(_batch.SPRITES)

__all__ = ["BATCHES", "ICONS", "RASTER", "SCENES", "SPRITES"]
