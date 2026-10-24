from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH2/Skyla_166.py"),
               collector_number=148, rarity=Rarities.Uncommon,
               guid="4540ecef-d467-59c6-aa74-93c021d51a53",
               set_code="XY8", key="XY8")
