from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Dugtrio_59.py"),
               collector_number=39, rarity=Rarities.Rare,
               guid="617657f1-ea22-5ab2-8955-16f17079f7f5",
               set_code="TwentiethAnn", key="TwentiethAnn")
