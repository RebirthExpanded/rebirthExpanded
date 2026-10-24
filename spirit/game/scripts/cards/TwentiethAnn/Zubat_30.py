from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/Zubat_31.py"),
               collector_number=30, rarity=Rarities.Common,
               guid="8f2fb105-43c8-5f47-a9be-2bc2a9b2d506",
               set_code="TwentiethAnn", key="TwentiethAnn")
