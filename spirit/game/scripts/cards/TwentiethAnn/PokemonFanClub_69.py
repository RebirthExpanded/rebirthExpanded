from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY10/PokemonFanClub_107.py"),
               collector_number=69, rarity=Rarities.Uncommon,
               guid="15785734-44ba-5d54-aeb8-a9cf18304c5a",
               set_code="TwentiethAnn", key="TwentiethAnn")
