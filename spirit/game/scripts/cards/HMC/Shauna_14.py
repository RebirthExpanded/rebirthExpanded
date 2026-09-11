"""Shauna (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 014/018).

Japan-only deck print of Shauna; same card as the Shauna
print in SWSH8.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=14, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
