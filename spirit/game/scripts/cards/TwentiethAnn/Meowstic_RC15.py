from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Meowstic_43.py"),
               collector_number=98, rarity=Rarities.Uncommon,
               guid="d2790377-ebb8-5e99-b33e-4b8dbcd900e8",
               set_code="TwentiethAnn", key="TwentiethAnn")
