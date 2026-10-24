from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/MrMime_97.py"),
               collector_number=52, rarity=Rarities.Uncommon,
               guid="90958556-9b46-5853-b9ca-ad96725df857",
               set_code="TwentiethAnn", key="TwentiethAnn")
