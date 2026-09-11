"""Ultra Ball (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 008/018).

Japan-only deck print of Ultra Ball; same card as the UltraBall
print in CZ.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=8, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
