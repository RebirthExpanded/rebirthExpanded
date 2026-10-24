from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY2/MCharizardEX_107.py"),
               collector_number=101, rarity=Rarities.RareUltra,
               guid="5a7eee27-971c-58f1-a9d2-fab897e7d64e",
               set_code="XY12", key="XY12")
