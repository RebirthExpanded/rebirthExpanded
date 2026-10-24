from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Cloyster_32.py"),
               collector_number=20, rarity=Rarities.Uncommon,
               guid="8d609f12-e008-58ab-8afb-86682088acab",
               set_code="TwentiethAnn", key="TwentiethAnn")
