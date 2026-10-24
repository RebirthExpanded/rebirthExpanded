from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/StrongEnergy_104.py"),
               collector_number=115, rarity=Rarities.Uncommon,
               guid="e102d84e-7447-5283-b2b4-db32af71a0c1",
               set_code="XY10", key="XY10")
