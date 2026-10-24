from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY5/Rhyhorn_74.py"),
               collector_number=49, rarity=Rarities.Common,
               guid="7163559c-ee64-57aa-bf33-5cf041dc6f2e",
               set_code="TwentiethAnn", key="TwentiethAnn")
