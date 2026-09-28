"""Wash Water Energy (SWSH - Vivid Voltage 165/185 -- JP S3a 073/076).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [W] Energy.
   Prevent all effects of attacks from your opponent's Pokemon done to the
   [W] Pokemon this card is attached to. (Existing effects are not removed.
   Damage is not an effect.)"
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.passives_common import attack_effect_shield_passive


def _water_holder(target, carrier):
    return carrier_pokemon(carrier) is target and (
        PokemonTypes.WATER.value in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = EnergyCardDef(
    guid="ea6c7c3d-b04f-547c-abca-e5e92777ed57",
    key="SWSH4",
    name="Wash Water Energy",
    display_name="Wash Water Energy",
    searchable_by=["Wash Water Energy", "Special", "WashWaterEnergy"],
    subtypes=["Special"],
    collector_number=165,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.WATER,
    is_special=True,
    passive=attack_effect_shield_passive(protects=_water_holder),
)
