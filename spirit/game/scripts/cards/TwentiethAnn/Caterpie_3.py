from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/Caterpie_1.py"),
               collector_number=3, rarity=Rarities.Common,
               guid="f76e0377-50dc-5258-8d1e-dc0d7c16ce79",
               set_code="TwentiethAnn", key="TwentiethAnn")
