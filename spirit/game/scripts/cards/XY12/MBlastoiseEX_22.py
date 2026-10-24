from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/MBlastoiseEX_30.py"),
               collector_number=22, rarity=Rarities.RareHoloEX,
               guid="71c754e2-41a1-574b-9e99-32c1cbe0ceda",
               set_code="XY12", key="XY12")
