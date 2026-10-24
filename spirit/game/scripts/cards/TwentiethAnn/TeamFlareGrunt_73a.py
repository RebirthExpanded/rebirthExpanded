from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY1/TeamFlareGrunt_129.py"),
               collector_number=117, rarity=Rarities.RareUltra,
               guid="17dd5516-3efc-5923-b693-7b8f83aaef09",
               set_code="TwentiethAnn", key="TwentiethAnn")
