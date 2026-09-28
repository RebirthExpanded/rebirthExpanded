"""Coating Metal Energy (SWSH - Vivid Voltage 163/185 -- JP S3a 075/076).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [M] Energy.
   The [M] Pokemon this card is attached to has no Weakness."
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import carrier_pokemon
from spirit.game.card_effects.passives_common import no_weakness_passive


def _metal_holder(target, carrier):
    return carrier_pokemon(carrier) is target and (
        PokemonTypes.METAL.value in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = EnergyCardDef(
    guid="c50584fd-a459-54fe-a292-e22d671bc1d6",
    key="SWSH4",
    name="Coating Metal Energy",
    display_name="Coating Metal Energy",
    searchable_by=["Coating Metal Energy", "Special", "CoatingMetalEnergy"],
    subtypes=["Special"],
    collector_number=163,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.METAL,
    is_special=True,
    passive=no_weakness_passive(protects=_metal_holder),
)
