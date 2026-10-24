from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SM7/RainbowEnergy_151.py"),
               collector_number=152, rarity=Rarities.Uncommon,
               guid="00b40821-ca09-5786-a58f-38a549f8bdf6",
               set_code="XY8", key="XY8")
