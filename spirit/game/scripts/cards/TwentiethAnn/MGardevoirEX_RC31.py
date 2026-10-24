from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY5/MGardevoirEX_106.py"),
               collector_number=114, rarity=Rarities.RareUltra,
               guid="5e1f0a43-a97b-5238-be02-4bacbc43fa77",
               set_code="TwentiethAnn", key="TwentiethAnn")
