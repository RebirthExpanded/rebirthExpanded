from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
               collector_number=126, rarity=Rarities.Uncommon,
               guid="8d7e9b30-ce96-5f75-9d48-a25c678fba68",
               set_code="XY5", key="XY5")
