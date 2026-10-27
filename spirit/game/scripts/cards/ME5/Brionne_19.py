"""Brionne (ME5 19 -- JP M5 018; English PBL/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0c7b950a-efdb-5eae-a1e2-d166f43b1993",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    display_name="Brionne",
    searchable_by=["Brionne", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Hyper Voice",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
    ],
)
