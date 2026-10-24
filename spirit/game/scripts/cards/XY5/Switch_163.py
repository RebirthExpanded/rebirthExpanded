from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=163, rarity=Rarities.RareSecret,
               guid="d25e1197-efa2-5328-a8dd-d1610471b288",
               set_code="XY5", key="XY5")
