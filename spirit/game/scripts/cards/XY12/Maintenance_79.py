from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Maintenance_96.py"),
               collector_number=79, rarity=Rarities.Uncommon,
               guid="4c25e3f7-ae72-5032-826e-19ab2b473fb3",
               set_code="XY12", key="XY12")
