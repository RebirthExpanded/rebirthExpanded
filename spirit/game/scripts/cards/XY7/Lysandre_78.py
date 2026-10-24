from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Lysandre_90.py"),
               collector_number=78, rarity=Rarities.Uncommon,
               guid="a1dcc4ec-3463-5c03-a295-68f0dada2c25",
               set_code="XY7", key="XY7")
