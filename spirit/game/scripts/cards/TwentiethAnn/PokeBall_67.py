from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/PokBall_137.py"),
               collector_number=67, rarity=Rarities.Uncommon,
               guid="d66bc6e5-8f65-5960-97eb-eef758905fd3",
               set_code="TwentiethAnn", key="TwentiethAnn")
