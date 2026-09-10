"""Raikou (JP M6a 162/103 -- 30th Celebrations).

The Amazing Rare Raikou reprinted for the anniversary set: same card as
Vivid Voltage 50, which the pool already has, so this is the thin reprint
stub with its own art and collector number.

Like the other two 30th Celebrations cards here, the English set is not out
yet, so it keeps the Japanese collector number.
"""

from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH4/Raikou_50.py"),
               collector_number=162, rarity=Rarities.Amazing,
               set_code="ME6A", key="ME6A")
