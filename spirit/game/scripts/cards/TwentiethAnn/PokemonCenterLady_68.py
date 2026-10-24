from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH1/PokemonCenterLady_176.py"),
               collector_number=68, rarity=Rarities.Uncommon,
               guid="6e0a8958-8017-596d-81de-c7752cf814c8",
               set_code="TwentiethAnn", key="TwentiethAnn")
