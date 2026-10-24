from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/Swirlix_68.py"),
               collector_number=102, rarity=Rarities.Uncommon,
               guid="a7fcb13a-7793-5313-b51a-c84fb828c431",
               set_code="TwentiethAnn", key="TwentiethAnn")
