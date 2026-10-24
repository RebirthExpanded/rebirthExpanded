from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY5/Tangela_4.py"),
               collector_number=8, rarity=Rarities.Common,
               guid="3b70d174-97bc-50f3-a35e-d8d597172229",
               set_code="TwentiethAnn", key="TwentiethAnn")
