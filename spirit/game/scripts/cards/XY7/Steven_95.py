from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Steven_90.py"),
               collector_number=95, rarity=Rarities.RareUltra,
               guid="2222e444-ca70-5b8a-9ba8-c8990419db06",
               set_code="XY7", key="XY7")
