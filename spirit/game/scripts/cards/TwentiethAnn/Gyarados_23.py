from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY7/Gyarados_20.py"),
               collector_number=23, rarity=Rarities.Rare,
               guid="c1e10c3d-ac62-5721-ab63-1fae461f6247",
               set_code="TwentiethAnn", key="TwentiethAnn")
