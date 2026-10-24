from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=93, rarity=Rarities.Uncommon,
               guid="95a767f8-9ba4-532b-ad5f-de0ef98316f4",
               set_code="XY6", key="XY6")
