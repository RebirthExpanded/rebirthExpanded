from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergyRetrieval_127.py"),
               collector_number=77, rarity=Rarities.Uncommon,
               guid="f9827398-87c0-583b-84f3-9bb314a7c29b",
               set_code="XY12", key="XY12")
