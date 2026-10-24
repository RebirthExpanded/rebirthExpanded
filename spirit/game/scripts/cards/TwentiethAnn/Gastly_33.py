from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Gastly_58.py"),
               collector_number=33, rarity=Rarities.Common,
               guid="de5886b5-f839-5a3b-a2a0-44ac85e0feb4",
               set_code="TwentiethAnn", key="TwentiethAnn")
