from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/MaxRevive_120.py"),
               collector_number=65, rarity=Rarities.Uncommon,
               guid="4ebc61ca-7af4-5584-b2af-df4d580918d5",
               set_code="TwentiethAnn", key="TwentiethAnn")
