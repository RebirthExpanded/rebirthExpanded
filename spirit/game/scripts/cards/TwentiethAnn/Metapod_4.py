from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Metapod_2.py"),
               collector_number=4, rarity=Rarities.Uncommon,
               guid="f6e13b26-32d6-5830-b468-475b5bd17942",
               set_code="TwentiethAnn", key="TwentiethAnn")
