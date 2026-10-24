from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Dodrio_117.py"),
               collector_number=56, rarity=Rarities.Rare,
               guid="94d7185f-c971-56c4-a9cf-29a66efd7a61",
               set_code="TwentiethAnn", key="TwentiethAnn")
