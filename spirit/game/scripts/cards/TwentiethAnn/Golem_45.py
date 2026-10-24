from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Golem_47.py"),
               collector_number=45, rarity=Rarities.RareHolo,
               guid="47b7e471-2cf9-5a79-9dc6-74aa616901a0",
               set_code="TwentiethAnn", key="TwentiethAnn")
