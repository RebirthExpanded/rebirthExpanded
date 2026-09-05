"""Super Rod (BW - Noble Victories 95/101).

Item.

  "Shuffle 3 in any combination of Pokemon and basic Energy cards from your
   discard pile back into your deck."

Max Rod's other half. Both read the same "in any combination of Pokemon and
basic Energy cards" pile, which is now pokemon_or_basic_energy in
card_effects/trainers.py; Max Rod puts up to 5 of them into the hand, this
shuffles 3 back into the deck.

choose_cards with no minimum means exactly 3, or everything if the discard
cannot supply 3 -- which is what the printed "Shuffle 3" (not "up to 3")
asks for. The SV reprint does say "up to 3"; this is the BW-era print, the
one the Japanese Dragon Selection card matches.

The English print drops the Japanese card's "show them to your opponent"
step, and nothing is lost: the discard pile is a public zone.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    has_pokemon_or_basic_energy_in_discard,
    super_rod,
)

card = ItemCardDef(
    guid="d45fb5ac-30e9-5b8b-b498-be0690ffa856",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item", "SuperRod"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=super_rod,
    condition=has_pokemon_or_basic_energy_in_discard,
)
