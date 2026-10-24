from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH2/Skyla_166.py"),
               collector_number=122, rarity=Rarities.RareUltra,
               guid="0d624a79-3a54-55f5-9d9d-c047f60f556b",
               set_code="XY9", key="XY9")
