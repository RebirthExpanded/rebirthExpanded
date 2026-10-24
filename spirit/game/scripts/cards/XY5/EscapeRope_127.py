from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH5/EscapeRope_125.py"),
               collector_number=127, rarity=Rarities.Uncommon,
               guid="7791ed2e-a676-504a-af84-ceaeee414e35",
               set_code="XY5", key="XY5")
