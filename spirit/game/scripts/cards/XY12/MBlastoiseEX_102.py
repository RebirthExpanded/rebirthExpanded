from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/MBlastoiseEX_30.py"),
               collector_number=102, rarity=Rarities.RareUltra,
               guid="a78a2f79-3d99-58e2-9f66-0c8e2ff9f862",
               set_code="XY12", key="XY12")
