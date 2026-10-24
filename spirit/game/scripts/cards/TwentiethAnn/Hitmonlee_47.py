from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Hitmonlee_47.py"),
               collector_number=47, rarity=Rarities.Rare,
               guid="f796cfdf-af61-5d89-9f0a-b14751409741",
               set_code="TwentiethAnn", key="TwentiethAnn")
