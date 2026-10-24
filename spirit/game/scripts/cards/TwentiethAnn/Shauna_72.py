from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH8/Shauna_240.py"),
               collector_number=72, rarity=Rarities.Uncommon,
               guid="3aff0924-4513-57cc-8415-035f756bf56b",
               set_code="TwentiethAnn", key="TwentiethAnn")
