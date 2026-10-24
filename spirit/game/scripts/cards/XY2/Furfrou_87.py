from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY0/Furfrou_32.py"),
               collector_number=87, rarity=Rarities.Uncommon,
               guid="0e694bdb-d6e0-58bc-b1b2-f2004975cf1c",
               set_code="XY2", key="XY2")
