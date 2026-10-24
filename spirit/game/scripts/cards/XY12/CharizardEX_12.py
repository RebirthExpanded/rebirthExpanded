from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/CharizardEX_12.py"),
               collector_number=12, rarity=Rarities.RareHoloEX,
               guid="f94ae01c-d5f3-5934-aa0a-c1cbd9de28f3",
               set_code="XY12", key="XY12")
