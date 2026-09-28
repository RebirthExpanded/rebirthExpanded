"""Stone Fighting Energy (SWSH - Vivid Voltage 164/185 -- JP S3a 076/076).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [F] Energy.
   The [F] Pokemon this card is attached to takes 20 less damage from
   attacks from your opponent's Pokemon (after applying Weakness and
   Resistance)."

Each attached copy takes its own 20 off.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.passives_common import takes_less_passive


def _fighting_holder(target, carrier):
    return carrier_pokemon(carrier) is target and (
        PokemonTypes.FIGHTING.value in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = EnergyCardDef(
    guid="547148db-8548-5873-a23b-fab024ff43d0",
    key="SWSH4",
    name="Stone Fighting Energy",
    display_name="Stone Fighting Energy",
    searchable_by=["Stone Fighting Energy", "Special", "StoneFightingEnergy"],
    subtypes=["Special"],
    collector_number=164,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.FIGHTING,
    is_special=True,
    passive=takes_less_passive(20, protects=_fighting_holder),
)
