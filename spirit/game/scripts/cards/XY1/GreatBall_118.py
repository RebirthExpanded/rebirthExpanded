from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/GreatBall_132.py"),
               collector_number=118, rarity=Rarities.Uncommon,
               guid="456f5154-79bb-567c-b554-91d300008321",
               set_code="XY1", key="XY1")
