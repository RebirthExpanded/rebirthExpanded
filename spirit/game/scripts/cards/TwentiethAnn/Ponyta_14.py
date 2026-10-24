from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Ponyta_14.py"),
               collector_number=14, rarity=Rarities.Common,
               guid="08392d77-75f6-5381-ae22-4fb3638dbbd3",
               set_code="TwentiethAnn", key="TwentiethAnn")
