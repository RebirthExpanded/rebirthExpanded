from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorSycamore_122.py"),
               collector_number=107, rarity=Rarities.Uncommon,
               guid="e3782a6d-4b9a-5ad2-835c-c0c187d6ac78",
               set_code="XY9", key="XY9")
