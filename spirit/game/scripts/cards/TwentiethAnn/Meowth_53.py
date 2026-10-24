from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Meowth_114.py"),
               collector_number=53, rarity=Rarities.Common,
               guid="367837ca-dd38-5ecc-9e48-96bc07bdbf2e",
               set_code="TwentiethAnn", key="TwentiethAnn")
