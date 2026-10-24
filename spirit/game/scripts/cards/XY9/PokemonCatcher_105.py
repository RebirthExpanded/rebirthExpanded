from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/PokemonCatcher_138.py"),
               collector_number=105, rarity=Rarities.Uncommon,
               guid="0b9bd788-cfb4-589f-b2fa-b64de85945cb",
               set_code="XY9", key="XY9")
