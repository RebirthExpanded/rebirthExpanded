from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Switch_144.py"),
               collector_number=38, rarity=Rarities.Common,
               guid="fc8951ea-c1c6-561c-8217-de2f148a34b6",
               set_code="XY0", key="XY0")
