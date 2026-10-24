from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY10/DevolutionSpray_95.py"),
               collector_number=76, rarity=Rarities.Uncommon,
               guid="fffc7ce3-749f-5fa5-94d5-c39526977302",
               set_code="XY12", key="XY12")
