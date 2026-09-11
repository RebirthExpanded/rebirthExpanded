"""Double Colorless Energy (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 018/018).

Japan-only deck print of Double Colorless Energy; same card as the DoubleColorlessEnergy
print in SM1.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SM1/DoubleColorlessEnergy_136.py"),
               collector_number=18, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
