from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/VenusaurEX_1.py"),
               collector_number=1, rarity=Rarities.RareHoloEX,
               guid="422367f7-a694-50b0-b15e-06abb0bcc56d",
               set_code="XY12", key="XY12")
