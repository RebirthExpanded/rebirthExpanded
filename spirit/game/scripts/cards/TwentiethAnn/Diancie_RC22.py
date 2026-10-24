from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/Diancie_71.py"),
               collector_number=105, rarity=Rarities.Uncommon,
               guid="0d32a5a3-f50d-5f48-8770-76f426544ba3",
               set_code="TwentiethAnn", key="TwentiethAnn")
