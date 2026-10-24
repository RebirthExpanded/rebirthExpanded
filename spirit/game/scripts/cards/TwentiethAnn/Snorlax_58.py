from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Snorlax_80.py"),
               collector_number=58, rarity=Rarities.Rare,
               guid="a56f6412-3ca1-593d-bc87-c7124f6e01e6",
               set_code="TwentiethAnn", key="TwentiethAnn")
