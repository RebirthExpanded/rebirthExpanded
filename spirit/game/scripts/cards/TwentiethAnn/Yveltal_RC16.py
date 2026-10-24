from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Yveltal_78.py"),
               collector_number=99, rarity=Rarities.Uncommon,
               guid="1b64a1b2-0840-5c6f-8d87-1e6d49018e85",
               set_code="TwentiethAnn", key="TwentiethAnn")
