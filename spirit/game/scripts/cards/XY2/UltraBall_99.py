from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=99, rarity=Rarities.Uncommon,
               guid="50b4f6a1-eb70-5633-b853-eacc2ae9fc62",
               set_code="XY2", key="XY2")
