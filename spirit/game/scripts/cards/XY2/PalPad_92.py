from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SWSH1/PalPad_172.py"),
               collector_number=92, rarity=Rarities.Uncommon,
               guid="75443892-5e97-5282-aa42-f2174aad5952",
               set_code="XY2", key="XY2")
