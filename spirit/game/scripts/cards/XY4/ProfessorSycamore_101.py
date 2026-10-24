from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorSycamore_122.py"),
               collector_number=101, rarity=Rarities.Uncommon,
               guid="91cca66d-51e9-5774-9a38-fa8a0ab97874",
               set_code="XY4", key="XY4")
