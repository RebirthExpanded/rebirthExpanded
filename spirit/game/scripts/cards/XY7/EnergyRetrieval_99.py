from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
               collector_number=99, rarity=Rarities.RareSecret,
               guid="490cf4ec-d7cc-599a-a191-8669ea2f4855",
               set_code="XY7", key="XY7")
