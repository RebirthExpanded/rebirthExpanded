from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/MCharizardEX_107.py"),
               collector_number=13, rarity=Rarities.RareHoloEX,
               guid="182cf86a-28d6-5896-b0dc-356917360f9a",
               set_code="XY12", key="XY12")
