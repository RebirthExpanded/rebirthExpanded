from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "SingleStrikeEnergy_141.py"),
               guid="a3759d28-263b-58da-96a8-1a4818d21e03",
               collector_number=183, rarity=Rarities.RareSecret,
               set_code="SWSH5", key="SWSH5")
