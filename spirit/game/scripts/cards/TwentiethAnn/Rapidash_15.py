from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Rapidash_15.py"),
               collector_number=15, rarity=Rarities.Rare,
               guid="e6e60c8b-9dc3-5b8d-8b50-aabb4d86c379",
               set_code="TwentiethAnn", key="TwentiethAnn")
