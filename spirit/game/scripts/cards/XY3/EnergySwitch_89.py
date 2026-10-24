from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergySwitch_129.py"),
               collector_number=89, rarity=Rarities.Uncommon,
               guid="57417a79-c9bc-515f-9810-0e32a2d51b9d",
               set_code="XY3", key="XY3")
