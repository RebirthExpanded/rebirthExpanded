from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "VGuardEnergy_169.py"),
               guid="ef958b98-1e55-58dd-8e39-ae69ba83ba9a",
               collector_number=215, rarity=Rarities.RareSecret,
               set_code="SWSH12", key="SWSH12")
