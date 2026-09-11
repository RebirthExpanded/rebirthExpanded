"""Switch (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 010/018).

Japan-only deck print of Switch; same card as the Switch
print in CZ.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=10, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
