from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Xerneas_96.py"),
               collector_number=81, rarity=Rarities.RareHolo,
               guid="bc521395-91a9-515d-9da9-c848344d1830",
               set_code="XY11", key="XY11")
