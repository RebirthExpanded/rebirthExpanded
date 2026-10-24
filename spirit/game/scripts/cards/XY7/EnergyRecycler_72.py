from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH5/EnergyRecycler_124.py"),
               collector_number=72, rarity=Rarities.Uncommon,
               guid="2eb32719-c95b-585f-8719-4108d11e70c0",
               set_code="XY7", key="XY7")
