from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Clefairy_69.py"),
               collector_number=50, rarity=Rarities.Common,
               guid="a4d4edae-9b75-5539-b3f8-6afbee9f78e2",
               set_code="TwentiethAnn", key="TwentiethAnn")
