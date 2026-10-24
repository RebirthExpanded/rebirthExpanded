from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/UltraBall_146.py"),
               collector_number=113, rarity=Rarities.Uncommon,
               guid="6fba3052-e071-5ce9-802c-ab86e8822d01",
               set_code="XY10", key="XY10")
