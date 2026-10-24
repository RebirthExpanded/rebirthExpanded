from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/Potion_139.py"),
               collector_number=106, rarity=Rarities.Uncommon,
               guid="0b7f5f46-38ed-5ece-96ab-9e445bcb12a6",
               set_code="XY9", key="XY9")
