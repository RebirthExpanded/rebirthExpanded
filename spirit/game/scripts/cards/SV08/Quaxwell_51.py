"""Quaxwell (SV08 51 -- JP SV7a 014; English SSP/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="85dbb4cb-032a-538f-8409-c3bc9e39585f",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    display_name="Quaxwell",
    searchable_by=["Quaxwell", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Aqua Edge",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
    ],
)
