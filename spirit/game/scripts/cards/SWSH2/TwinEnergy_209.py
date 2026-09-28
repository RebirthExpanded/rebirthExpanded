from spirit.game.data_utils import reprint, sibling_card
from spirit.game.attributes import Rarities

card = reprint(sibling_card(__file__, "TwinEnergy_174.py"),
               guid="96dbb5dc-bb45-5d47-8d18-dc27698b75a3",
               collector_number=209, rarity=Rarities.RareSecret,
               set_code="SWSH2", key="SWSH2")
