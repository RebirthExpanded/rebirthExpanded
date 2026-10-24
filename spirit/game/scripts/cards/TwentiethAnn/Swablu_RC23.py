from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Swablu_73.py"),
               collector_number=106, rarity=Rarities.Common,
               guid="9a86c11a-7e5c-5be9-ac91-f5e8a56934a8",
               set_code="TwentiethAnn", key="TwentiethAnn")
