from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Yveltal_78.py"),
               collector_number=65, rarity=Rarities.RareHolo,
               guid="aec7025a-044e-52e7-ae62-f053bc22e49b",
               set_code="XY11", key="XY11")
