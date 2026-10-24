from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Doduo_116.py"),
               collector_number=55, rarity=Rarities.Common,
               guid="0f166815-c646-5b68-a0bf-b129836329e7",
               set_code="TwentiethAnn", key="TwentiethAnn")
