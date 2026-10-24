from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY0/Furfrou_32.py"),
               collector_number=90, rarity=Rarities.Uncommon,
               guid="179c4def-75f9-557d-a970-6d5730eed36d",
               set_code="XY4", key="XY4")
