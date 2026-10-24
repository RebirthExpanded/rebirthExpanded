from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Potion_139.py"),
               collector_number=37, rarity=Rarities.Common,
               guid="fc5b182c-524d-53d2-8d5b-e92871f18317",
               set_code="XY0", key="XY0")
