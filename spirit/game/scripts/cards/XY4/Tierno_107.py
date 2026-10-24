from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY0/Tierno_39.py"),
               collector_number=107, rarity=Rarities.Uncommon,
               guid="29b0a32c-164d-51bc-9f42-b674e850bcee",
               set_code="XY4", key="XY4")
