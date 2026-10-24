from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Jynx_37.py"),
               collector_number=36, rarity=Rarities.Rare,
               guid="c1460c34-7ece-5391-879f-8dc86a03a634",
               set_code="TwentiethAnn", key="TwentiethAnn")
