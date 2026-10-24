from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH5/ExpShare_126.py"),
               collector_number=128, rarity=Rarities.Uncommon,
               guid="ea1c08d0-4fa1-5ad8-ab95-1a01337f9cd4",
               set_code="XY5", key="XY5")
