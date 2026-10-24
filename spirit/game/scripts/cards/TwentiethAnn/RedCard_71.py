from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/RedCard_124.py"),
               collector_number=71, rarity=Rarities.Uncommon,
               guid="e5e855ca-2af9-536e-a349-7dcf5d43bfc1",
               set_code="TwentiethAnn", key="TwentiethAnn")
