from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Swablu_73.py"),
               collector_number=124, rarity=Rarities.Common,
               guid="a829dce5-c3f5-505b-af31-a1e92df13843",
               set_code="XY8", key="XY8")
