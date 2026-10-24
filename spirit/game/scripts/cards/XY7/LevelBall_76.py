from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH5/LevelBall_129.py"),
               collector_number=76, rarity=Rarities.Uncommon,
               guid="543b23c8-9679-5054-a8c6-3f96358f1781",
               set_code="XY7", key="XY7")
