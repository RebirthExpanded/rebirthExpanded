from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=111, rarity=Rarities.Uncommon,
               guid="45af2673-7da9-5e60-a2a3-6d6ea7fdc535",
               set_code="XY10", key="XY10")
