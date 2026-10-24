from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH1/PokemonCenterLady_176.py"),
               collector_number=105, rarity=Rarities.RareUltra,
               guid="fd84c276-2119-5dfe-9085-790361bbb4ae",
               set_code="XY2", key="XY2")
