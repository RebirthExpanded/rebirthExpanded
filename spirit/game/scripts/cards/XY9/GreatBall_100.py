from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/GreatBall_132.py"),
               collector_number=100, rarity=Rarities.Uncommon,
               guid="c83cff56-2d11-5c3f-b62f-ad5e30308098",
               set_code="XY9", key="XY9")
