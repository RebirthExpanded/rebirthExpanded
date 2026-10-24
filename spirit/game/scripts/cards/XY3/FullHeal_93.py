from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH2/FullHeal_159.py"),
               collector_number=93, rarity=Rarities.Uncommon,
               guid="df84575c-78ae-544f-bc8d-47879e699761",
               set_code="XY3", key="XY3")
