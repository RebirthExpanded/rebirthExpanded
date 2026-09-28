"""Hiding Darkness Energy (SWSH - Darkness Ablaze 175/189 -- JP S2a 069/070).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [D] Energy.
   The [D] Pokemon this card is attached to has no Retreat Cost."
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.passives_common import retreat_free_when


def _darkness_holder(target, carrier):
    return carrier_pokemon(carrier) is target and (
        PokemonTypes.DARKNESS.value in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = EnergyCardDef(
    guid="709ead1d-954d-5d13-af34-3c68e04cff49",
    key="SWSH3",
    name="Hiding Darkness Energy",
    display_name="Hiding Darkness Energy",
    searchable_by=["Hiding Darkness Energy", "Special", "HidingDarknessEnergy"],
    subtypes=["Special"],
    collector_number=175,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.DARKNESS,
    is_special=True,
    passive=retreat_free_when(_darkness_holder),
)
