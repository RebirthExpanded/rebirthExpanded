from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../SM7/RainbowEnergy_151.py"),
               collector_number=131, rarity=Rarities.Uncommon,
               guid="06f5ecd3-fcc2-589f-b1fb-088479bd5b58",
               set_code="XY1", key="XY1")
