from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Magmar_10.py"),
               collector_number=16, rarity=Rarities.Common,
               guid="b3d2c64f-763f-540a-9940-16b0fe019e40",
               set_code="TwentiethAnn", key="TwentiethAnn")
