from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/BlastoiseEX_142.py"),
               collector_number=21, rarity=Rarities.RareHoloEX,
               guid="b6adb92a-9124-5d61-b72b-4cebec4cedc2",
               set_code="XY12", key="XY12")
