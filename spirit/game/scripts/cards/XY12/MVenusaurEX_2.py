from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/MVenusaurEX_2.py"),
               collector_number=2, rarity=Rarities.RareHoloEX,
               guid="4a5038a4-8c36-594c-b93f-b317d92b2520",
               set_code="XY12", key="XY12")
