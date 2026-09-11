"""Professor Sycamore (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 016/018).

Japan-only deck print of Professor Sycamore; same card as the ProfessorSycamore
print in XY1.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorSycamore_122.py"),
               collector_number=16, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
