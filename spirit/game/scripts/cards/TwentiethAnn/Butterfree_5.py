from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Butterfree_3.py"),
               collector_number=5, rarity=Rarities.RareHolo,
               guid="87d0e2ed-2f7b-515d-9608-6626805ba4b2",
               set_code="TwentiethAnn", key="TwentiethAnn")
