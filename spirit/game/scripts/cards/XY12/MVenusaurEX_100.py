from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/MVenusaurEX_2.py"),
               collector_number=100, rarity=Rarities.RareUltra,
               guid="5645fa61-12db-5a22-b751-965f28a10bf8",
               set_code="XY12", key="XY12")
