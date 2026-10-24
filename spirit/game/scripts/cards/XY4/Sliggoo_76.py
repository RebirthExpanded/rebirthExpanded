from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Sliggoo_73.py"),
               collector_number=76, rarity=Rarities.Uncommon,
               guid="a703b7c0-ec06-54d7-ac52-29157df048bb",
               set_code="XY4", key="XY4")
