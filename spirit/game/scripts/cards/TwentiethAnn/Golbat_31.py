from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/Golbat_32.py"),
               collector_number=31, rarity=Rarities.Uncommon,
               guid="4e98eaee-c646-5e3f-a359-1b1f45c14e8d",
               set_code="TwentiethAnn", key="TwentiethAnn")
