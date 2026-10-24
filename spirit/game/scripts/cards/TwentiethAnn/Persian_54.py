from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY7/Persian_62.py"),
               collector_number=54, rarity=Rarities.Uncommon,
               guid="592e104a-7da2-5dd7-991c-59f18b3ec172",
               set_code="TwentiethAnn", key="TwentiethAnn")
