from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Hitmonchan_48.py"),
               collector_number=48, rarity=Rarities.Rare,
               guid="5a62712d-45d4-5e25-b714-c9d39ef9f054",
               set_code="TwentiethAnn", key="TwentiethAnn")
