from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Judge_235.py"),
               collector_number=143, rarity=Rarities.Uncommon,
               guid="4cffeac9-bfc2-5f59-87b7-dabc51af68f9",
               set_code="XY8", key="XY8")
