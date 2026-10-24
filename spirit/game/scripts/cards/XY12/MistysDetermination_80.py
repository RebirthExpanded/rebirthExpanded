from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY9/MistysDetermination_104.py"),
               collector_number=80, rarity=Rarities.Uncommon,
               guid="63afda62-82d4-572b-87d4-2b9ade7723d9",
               set_code="XY12", key="XY12")
