from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH9/FreshWaterSet_139.py"),
               collector_number=129, rarity=Rarities.Uncommon,
               guid="604dd107-9002-5356-aaef-b226b6b00852",
               set_code="XY5", key="XY5")
