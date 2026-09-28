"""Fusion Strike Energy (SWSH - Fusion Strike 244/264).

Special Energy.

  "This card can only be attached to a Fusion Strike Pokemon. If this card
   is attached to anything other than a Fusion Strike Pokemon, discard this
   card. As long as this card is attached to a Pokemon, it provides every
   type of Energy but provides only 1 Energy at a time. Prevent all effects
   of your opponent's Pokemon's Abilities done to the Pokemon this card is
   attached to."

The Fusion Strike restriction, Rainbow Energy's type list, and Stealthy
Hood's shield against the opponent's Ability effects.
"""

from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import ability_effect_shield_passive


def is_fusion_strike(pokemon) -> bool:
    return "Fusion Strike" in subtypes_for(pokemon.archetype_id)


card = EnergyCardDef(
    guid="a1be9557-4439-5c31-8c90-51a75824090f",
    key="SWSH8",
    name="Fusion Strike Energy",
    display_name="Fusion Strike Energy",
    searchable_by=["Fusion Strike Energy", "Fusion Strike", "Special"],
    subtypes=["Fusion Strike", "Special"],
    collector_number=244,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_fusion_strike,
    discard_if_invalid=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=ability_effect_shield_passive(),
)
