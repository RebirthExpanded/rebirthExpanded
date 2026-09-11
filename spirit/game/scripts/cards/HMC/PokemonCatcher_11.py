"""Pokémon Catcher (JP XY Hyper Metal Chain Deck 60 "Dialga-EX + Aegislash-EX" -- HMC 011/018).

Japan-only deck print of Pokémon Catcher; same card as the PokemonCatcher
print in CZ. This is the coin-flip (2013 errata) text.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(sibling_card(__file__, "../CZ/PokemonCatcher_138.py"),
               collector_number=11, rarity=Rarities.Uncommon,
               set_code="HMC", key="HMC")
