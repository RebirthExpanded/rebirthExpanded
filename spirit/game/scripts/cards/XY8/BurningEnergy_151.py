"""Burning Energy (XY - BREAKthrough 151/162 -- JP XY8 059/059, Red Flash).

Special Energy.

  "This card can only be attached to [R] Pokemon. This card provides [R]
   Energy only while this card is attached to a [R] Pokemon. If this card
   is discarded by an effect of an attack used by the [R] Pokemon this card
   is attached to, attach it to that Pokemon after the attack's damage and
   effects. (If this card is attached to anything other than a [R] Pokemon,
   discard this card.)"

Boomerang Energy (SV06)'s reattach hook on Strong Energy's type-locked
shape.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import boomerang_reattach
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _fire_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.FIRE)


card = EnergyCardDef(
    guid="e636ecbe-7079-550e-afb5-952890983e0d",
    key="XY8",
    name="Burning Energy",
    display_name="Burning Energy",
    searchable_by=["Burning Energy", "Special", "BurningEnergy"],
    subtypes=["Special"],
    collector_number=151,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIRE,
    is_special=True,
    attach_to=_fire_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.FIRE]],
    on_discarded_by_carrier_attack=boomerang_reattach,
)
