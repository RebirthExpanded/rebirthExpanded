from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergySwitch_129.py"),
               collector_number=109, rarity=Rarities.RareSecret,
               guid="7b5c103a-b1e2-504a-808f-86cd15d3c1f0",
               set_code="XY6", key="XY6")
