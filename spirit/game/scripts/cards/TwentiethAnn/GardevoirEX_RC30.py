from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY5/GardevoirEX_105.py"),
               collector_number=113, rarity=Rarities.RareUltra,
               guid="c00cece1-4af6-5c09-ac9f-e778a0c9feba",
               set_code="TwentiethAnn", key="TwentiethAnn")
