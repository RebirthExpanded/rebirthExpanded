from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY9/MistysDetermination_104.py"),
               collector_number=108, rarity=Rarities.RareUltra,
               guid="8b744459-4c3c-5148-a10a-73465def16e9",
               set_code="XY12", key="XY12")
