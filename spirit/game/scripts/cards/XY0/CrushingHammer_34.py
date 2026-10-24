from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/CrushingHammer_125.py"),
               collector_number=34, rarity=Rarities.Common,
               guid="6a7b2ef9-fce1-5857-a9ce-0272947f30c2",
               set_code="XY0", key="XY0")
