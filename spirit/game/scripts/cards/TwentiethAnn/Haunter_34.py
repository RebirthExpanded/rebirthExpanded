from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Haunter_59.py"),
               collector_number=34, rarity=Rarities.Uncommon,
               guid="e77152af-7db8-5291-9ade-d7544195b1b1",
               set_code="TwentiethAnn", key="TwentiethAnn")
