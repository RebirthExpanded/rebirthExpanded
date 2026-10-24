from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Pikachu_42.py"),
               collector_number=26, rarity=Rarities.Common,
               guid="61c53a16-e701-5d92-921e-412a38689e1c",
               set_code="TwentiethAnn", key="TwentiethAnn")
