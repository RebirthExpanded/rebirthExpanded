from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../XY6/Zapdos_23.py"),
               collector_number=29, rarity=Rarities.RareHolo,
               guid="075348cb-55fc-500d-961d-48b872ae0ca4",
               set_code="TwentiethAnn", key="TwentiethAnn")
