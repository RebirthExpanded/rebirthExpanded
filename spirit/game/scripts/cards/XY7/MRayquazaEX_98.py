from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/MRayquazaEX_105.py"),
               collector_number=98, rarity=Rarities.RareSecret,
               guid="8b393177-5104-5466-b5f5-984026936a0c",
               set_code="XY7", key="XY7")
