from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorSycamore_122.py"),
               collector_number=126, rarity=Rarities.Uncommon,
               guid="952ae9ea-85e3-5416-8c54-ffe0568cea65",
               set_code="XY9", key="XY9")
