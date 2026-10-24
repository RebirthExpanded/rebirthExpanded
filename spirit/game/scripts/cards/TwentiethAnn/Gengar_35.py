from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY8/Gengar_60.py"),
               collector_number=35, rarity=Rarities.RareHolo,
               guid="af12b504-3efa-5f74-9427-58dc78712ee7",
               set_code="TwentiethAnn", key="TwentiethAnn")
