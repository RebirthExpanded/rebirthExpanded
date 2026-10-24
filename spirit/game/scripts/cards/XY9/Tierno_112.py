from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY0/Tierno_39.py"),
               collector_number=112, rarity=Rarities.Uncommon,
               guid="4998942b-1b73-5f08-8bc4-779c04c31b3d",
               set_code="XY9", key="XY9")
