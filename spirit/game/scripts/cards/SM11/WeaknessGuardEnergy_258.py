"""Weakness Guard Energy (SM - Unified Minds 213/236 -- JP SM11 090/094).

Special Energy.

  "This card provides [C] Energy.
   The Pokemon this card is attached to has no Weakness."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.data_utils import EnergyCardDef

card = EnergyCardDef(
    guid='1a405954-c087-5c16-b5c4-2a7f45b546df',
    key='SM11',
    name="Weakness Guard Energy",
    display_name="Weakness Guard Energy",
    searchable_by=["Weakness Guard Energy", "Special", "WeaknessGuardEnergy"],
    subtypes=["Special"],
    collector_number=258,
    set_code='SM11',
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=no_weakness_passive(),
)
