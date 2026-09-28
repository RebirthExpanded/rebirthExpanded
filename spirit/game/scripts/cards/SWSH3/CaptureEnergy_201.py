from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "../SWSH2/CaptureEnergy_171.py"),
               guid="40417df0-ec7f-5d30-90a8-6123062625b4",
               collector_number=201, rarity=Rarities.RareSecret,
               set_code="SWSH3", key="SWSH3")
