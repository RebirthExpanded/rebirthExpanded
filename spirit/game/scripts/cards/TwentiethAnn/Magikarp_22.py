from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY7/Magikarp_19.py"),
               collector_number=22, rarity=Rarities.Common,
               guid="79016ff5-4fc6-5f64-94d9-682a04deda9f",
               set_code="TwentiethAnn", key="TwentiethAnn")
