"""Cynthia's Power Weight (SV - Destined Rivals 162/182 -- JP SV9a 060/063).

Pokemon Tool.

  "The Cynthia's Pokemon this card is attached to gets +70 HP."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool
from spirit.game.data_utils import PokemonToolCardDef, def_for


def _is_cynthias(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Cynthia's ")


card = PokemonToolCardDef(
    guid="068b20b3-fa8b-5137-a53a-e9d4bc9a436f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasPowerWeight.Name",
    display_name="Cynthia's Power Weight",
    searchable_by=["Cynthia's Power Weight", "Pokémon Tool", "CynthiasPowerWeight"],
    subtypes=["Pokémon Tool"],
    collector_number=162,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(70, holder_pred=_is_cynthias),
)
