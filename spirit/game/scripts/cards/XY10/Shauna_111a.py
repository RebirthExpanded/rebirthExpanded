from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=129, rarity=Rarities.RareUltra,
               guid="179c31ec-0ced-5af4-9eba-1424132ea1e9",
               set_code="XY10", key="XY10")
