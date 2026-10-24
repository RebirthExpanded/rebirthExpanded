from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=88, rarity=Rarities.Uncommon,
               guid="675f5b04-41be-5b3c-8610-da16a9f81e8d",
               set_code="XY12", key="XY12")
