from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/TeamFlareGrunt_129.py"),
               collector_number=73, rarity=Rarities.Uncommon,
               guid="44b0ed40-5fb4-500d-9ba8-be00d2f93023",
               set_code="TwentiethAnn", key="TwentiethAnn")
