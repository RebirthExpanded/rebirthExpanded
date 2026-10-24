from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Articuno_16.py"),
               collector_number=25, rarity=Rarities.RareHolo,
               guid="a0dd86c9-449d-5554-8b14-e1e61ef61764",
               set_code="TwentiethAnn", key="TwentiethAnn")
