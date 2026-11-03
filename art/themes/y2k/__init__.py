"""Y2K theme art: glossy vector critters, scenes and icons, drawn by kit.py.

A vector theme for the engine (art/generate.py): VECTOR, SPRITES, BATCHES, SCENES, ICONS.
Each batch file has CRITTERS (name -> Critter); this module turns each into SPRITES
(name -> a function of the status). A new batch file must be imported here and added to BATCHES.
"""

from functools import partial

from . import batch_a, batch_b, batch_c
from .kit import sprite
from .scenes import ICONS, SCENES

VECTOR = True
BATCHES = {"batch_a": batch_a, "batch_b": batch_b, "batch_c": batch_c}
SPRITES = {}

for _name, _batch in BATCHES.items():
    assert not set(_batch.CRITTERS) & set(SPRITES), f"{_name}: critter name taken"
    _batch.SPRITES = {_critter: partial(sprite, _c) for _critter, _c in _batch.CRITTERS.items()}
    SPRITES.update(_batch.SPRITES)

__all__ = ["BATCHES", "ICONS", "SCENES", "SPRITES", "VECTOR"]
