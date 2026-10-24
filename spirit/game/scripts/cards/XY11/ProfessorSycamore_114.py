from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorSycamore_122.py"),
               collector_number=114, rarity=Rarities.RareUltra,
               guid="07ae5c3a-de5d-574f-8da6-9e492628c50e",
               set_code="XY11", key="XY11")
