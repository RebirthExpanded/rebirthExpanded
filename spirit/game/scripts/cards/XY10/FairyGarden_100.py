from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/FairyGarden_117.py"),
               collector_number=100, rarity=Rarities.Uncommon,
               guid="d8690750-dcb9-57ad-95fa-d13f254cef14",
               set_code="XY10", key="XY10")
