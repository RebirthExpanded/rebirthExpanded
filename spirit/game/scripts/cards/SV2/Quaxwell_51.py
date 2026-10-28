"""Quaxwell (SV2 51 -- JP SV1a 029; English PAL/207, PAL/51, SVP/83). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="bc2ecaad-e76a-57dc-83ca-ad3ad9092cf9",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    display_name="Quaxwell",
    searchable_by=["Quaxwell", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
