from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/RareCandy_141.py"),
               collector_number=135, rarity=Rarities.Uncommon,
               guid="a1fc4a8b-8c18-56fa-a213-8524cd7ec8ec",
               set_code="XY5", key="XY5")
