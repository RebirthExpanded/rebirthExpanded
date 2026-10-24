from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=104, rarity=Rarities.Uncommon,
               guid="44a9e31a-f5e8-58a2-b918-b7de65bb74e2",
               set_code="XY4", key="XY4")
