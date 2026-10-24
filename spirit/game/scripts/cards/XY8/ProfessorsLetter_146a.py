from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/ProfessorsLetter_123.py"),
               collector_number=165, rarity=Rarities.Uncommon,
               guid="38c48494-617e-54a5-81b8-b4c0e3cdcf77",
               set_code="XY8", key="XY8")
