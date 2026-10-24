from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY5/GardevoirSpiritLink_130.py"),
               collector_number=101, rarity=Rarities.Uncommon,
               guid="b30be1a7-7788-52fd-bfc2-b5d272fac7ad",
               set_code="XY11", key="XY11")
