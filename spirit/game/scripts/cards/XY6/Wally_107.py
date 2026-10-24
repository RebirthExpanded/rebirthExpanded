"""Wally (XY - Roaring Skies 107/108, full art) -- the same card as Wally 94."""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "Wally_94.py"),
               collector_number=107, rarity=Rarities.RareUltra,
               guid="5d792bae-2a1a-5062-ab73-98ed56ad628b")
