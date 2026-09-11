"""VS Seeker (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 009/018).

Japan-only deck print of VS Seeker; same card as the VSSeeker
print in XY4. The Japanese name is Battle Searcher (バトルサーチャー).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/VSSeeker_109.py"),
               collector_number=9, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
