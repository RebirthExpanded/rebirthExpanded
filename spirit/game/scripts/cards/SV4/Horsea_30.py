"""Horsea (SV4 30 -- JP SV4K 017; English PAR/30, SVP/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1fb781b8-379d-51a0-bcae-0add8965ede9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Hook",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
