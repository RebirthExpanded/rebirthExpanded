from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/PokBall_137.py"),
               collector_number=35, rarity=Rarities.Common,
               guid="49a0c826-6d02-516d-9152-a107bb902d8a",
               set_code="XY0", key="XY0")
