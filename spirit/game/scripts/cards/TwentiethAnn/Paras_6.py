from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Paras_1.py"),
               collector_number=6, rarity=Rarities.Common,
               guid="78155759-f337-5f70-9154-1a04cca6b375",
               set_code="TwentiethAnn", key="TwentiethAnn")
