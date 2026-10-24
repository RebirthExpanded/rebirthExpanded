from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=91, rarity=Rarities.Uncommon,
               guid="89bf02c0-a32e-54da-b22b-f077f6491061",
               set_code="XY6", key="XY6")
