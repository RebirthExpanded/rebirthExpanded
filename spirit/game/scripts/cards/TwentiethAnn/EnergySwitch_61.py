from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/EnergySwitch_129.py"),
               collector_number=61, rarity=Rarities.Uncommon,
               guid="846c222c-33ab-5929-9d29-b7de59dcd949",
               set_code="TwentiethAnn", key="TwentiethAnn")
