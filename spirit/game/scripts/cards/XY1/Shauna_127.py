from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=127, rarity=Rarities.Uncommon,
               guid="9d9df75a-5db1-525f-bccf-b33836e7de1e",
               set_code="XY1", key="XY1")
