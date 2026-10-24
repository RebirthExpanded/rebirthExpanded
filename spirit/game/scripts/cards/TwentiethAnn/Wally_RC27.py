from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Wally_107.py"),
               collector_number=110, rarity=Rarities.Uncommon,
               guid="b5cb4fd0-47bb-5f4a-aa12-ab674497aecd",
               set_code="TwentiethAnn", key="TwentiethAnn")
