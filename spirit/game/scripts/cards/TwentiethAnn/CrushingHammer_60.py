from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/CrushingHammer_125.py"),
               collector_number=60, rarity=Rarities.Uncommon,
               guid="b0292efc-b546-59bd-bebe-1c5e813452f4",
               set_code="TwentiethAnn", key="TwentiethAnn")
