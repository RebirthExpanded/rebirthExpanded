from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/PokemonCatcher_138.py"),
               collector_number=36, rarity=Rarities.Common,
               guid="47557205-d523-5a0d-be55-5b338227c78f",
               set_code="XY0", key="XY0")
