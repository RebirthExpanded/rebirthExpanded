from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY4/VSSeeker_109.py"),
               collector_number=110, rarity=Rarities.RareSecret,
               guid="f499207a-db1a-5bdd-a33c-776871533a3f",
               set_code="XY6", key="XY6")
