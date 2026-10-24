from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Pinsir_3.py"),
               collector_number=9, rarity=Rarities.Rare,
               guid="22b2fca0-2f14-522c-a797-6652617d4056",
               set_code="TwentiethAnn", key="TwentiethAnn")
