from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Geodude_45.py"),
               collector_number=43, rarity=Rarities.Common,
               guid="905d68c7-fb08-5499-b639-092fa6522cb7",
               set_code="TwentiethAnn", key="TwentiethAnn")
