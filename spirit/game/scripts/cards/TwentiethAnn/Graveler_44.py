from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Graveler_46.py"),
               collector_number=44, rarity=Rarities.Uncommon,
               guid="4c70b631-5a7c-5f9f-b6fe-188f895576a5",
               set_code="TwentiethAnn", key="TwentiethAnn")
