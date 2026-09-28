"""Wonder Energy (XY - Primal Clash 144/160 -- JP XY5 070/070 (Tidal Storm)).

Special Energy.

  "This card can only be attached to [Y] Pokemon. This card provides [Y]
   Energy only while this card is attached to a [Y] Pokemon. Prevent all
   effects of your opponent's attacks, except damage, done to the [Y]
   Pokemon this card is attached to. (If this card is attached to anything
   other than a [Y] Pokemon, discard this card.)"

Strong Energy (XY3)'s type-locked shape: attach_to + discard_if_invalid.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.card_effects.passives_common import attack_effect_shield_passive


def _fairy_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.FAIRY)


card = EnergyCardDef(
    guid="1b6ebe1c-0bca-5cf9-b6f0-c8473403b620",
    key="XY5",
    name="Wonder Energy",
    display_name="Wonder Energy",
    searchable_by=["Wonder Energy", "Special", "WonderEnergy"],
    subtypes=["Special"],
    collector_number=144,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FAIRY,
    is_special=True,
    attach_to=_fairy_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.FAIRY]],
    passive=attack_effect_shield_passive(),
)
