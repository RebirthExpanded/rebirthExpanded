from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/TrainersMail_92.py"),
               collector_number=100, rarity=Rarities.RareSecret,
               guid="ab14acf2-41de-5fb0-b424-f7c10e446763",
               set_code="XY7", key="XY7")
