from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Revive_88.py"),
               collector_number=85, rarity=Rarities.Uncommon,
               guid="b5ed74e1-7938-5542-83a5-ec04d5bf4aa0",
               set_code="XY12", key="XY12")
