from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Machamp_46.py"),
               collector_number=42, rarity=Rarities.RareHolo,
               guid="d378bbaf-bd22-59c9-ad1d-0246567ece35",
               set_code="TwentiethAnn", key="TwentiethAnn")
