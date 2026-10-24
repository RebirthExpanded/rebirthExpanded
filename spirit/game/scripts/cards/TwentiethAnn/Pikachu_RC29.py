from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/Pikachu_42.py"),
               collector_number=112, rarity=Rarities.RareUltra,
               guid="80fb5297-f1ae-5669-a199-6853d0ebc67f",
               set_code="TwentiethAnn", key="TwentiethAnn")
