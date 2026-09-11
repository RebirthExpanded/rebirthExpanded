"""Roller Skates (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 013/018).

Japan-only deck print of Roller Skates; same card as the RollerSkates
print in XY1.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/RollerSkates_125.py"),
               collector_number=13, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
