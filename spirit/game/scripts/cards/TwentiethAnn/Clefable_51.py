from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY3/Clefable_71.py"),
               collector_number=51, rarity=Rarities.Uncommon,
               guid="c6de8f1d-9d99-5a4b-93c6-df105822ee27",
               set_code="TwentiethAnn", key="TwentiethAnn")
