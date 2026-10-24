from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Diglett_58.py"),
               collector_number=38, rarity=Rarities.Common,
               guid="b1ac1cda-832a-5ba3-9613-e98f6a8ad264",
               set_code="TwentiethAnn", key="TwentiethAnn")
