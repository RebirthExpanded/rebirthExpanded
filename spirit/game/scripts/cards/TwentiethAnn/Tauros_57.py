from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Tauros_100.py"),
               collector_number=57, rarity=Rarities.Rare,
               guid="ebe48d4d-02ef-59e4-b0fe-0e68ef2066a8",
               set_code="TwentiethAnn", key="TwentiethAnn")
