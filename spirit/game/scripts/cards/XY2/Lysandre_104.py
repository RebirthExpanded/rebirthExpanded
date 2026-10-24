from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Lysandre_90.py"),
               collector_number=104, rarity=Rarities.RareUltra,
               guid="6e2ee7b2-2b80-5617-ab6f-e8de5d58a8a9",
               set_code="XY2", key="XY2")
