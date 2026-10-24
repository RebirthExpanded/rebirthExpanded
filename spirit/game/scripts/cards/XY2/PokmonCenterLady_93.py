from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH1/PokemonCenterLady_176.py"),
               collector_number=93, rarity=Rarities.Uncommon,
               guid="8b9ea630-8bdf-59b3-aefc-d81ef601d49e",
               set_code="XY2", key="XY2")
