from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Parasect_2.py"),
               collector_number=7, rarity=Rarities.Rare,
               guid="f72f52cd-021b-5981-b90b-d4e8156a775f",
               set_code="TwentiethAnn", key="TwentiethAnn")
