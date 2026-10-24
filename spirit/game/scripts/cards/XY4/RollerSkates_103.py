from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/RollerSkates_125.py"),
               collector_number=103, rarity=Rarities.Uncommon,
               guid="f8f1569d-092a-56a8-8bdc-83f0902acc95",
               set_code="XY4", key="XY4")
