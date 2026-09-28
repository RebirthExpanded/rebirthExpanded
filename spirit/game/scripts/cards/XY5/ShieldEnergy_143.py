"""Shield Energy (XY - Primal Clash 143/160 -- JP XY5 070/070 (Gaia Volcano)).

Special Energy.

  "This card can only be attached to [M] Pokemon. This card provides [M]
   Energy only while this card is attached to a [M] Pokemon. Any damage
   done to the [M] Pokemon this card is attached to by attacks from your
   opponent's Pokemon is reduced by 10 (after applying Weakness and
   Resistance). (If this card is attached to anything other than a [M]
   Pokemon, discard this card.)"

Strong Energy (XY3)'s type-locked shape: attach_to + discard_if_invalid.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type
from spirit.game.card_effects.passives_common import takes_less_passive


def _metal_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.METAL)


card = EnergyCardDef(
    guid="f7a64bd8-83ff-588e-80af-ba9b21b7172e",
    key="XY5",
    name="Shield Energy",
    display_name="Shield Energy",
    searchable_by=["Shield Energy", "Special", "ShieldEnergy"],
    subtypes=["Special"],
    collector_number=143,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    attach_to=_metal_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.METAL]],
    passive=takes_less_passive(10),
)
