from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH2/FullHeal_159.py"),
               collector_number=78, rarity=Rarities.Uncommon,
               guid="42fe7d77-0208-55ed-af0d-799ba83d0b1e",
               set_code="XY12", key="XY12")
