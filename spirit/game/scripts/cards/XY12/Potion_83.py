from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Potion_139.py"),
               collector_number=83, rarity=Rarities.Uncommon,
               guid="73751f7c-efe3-5a0a-8c04-f59dac56911a",
               set_code="XY12", key="XY12")
