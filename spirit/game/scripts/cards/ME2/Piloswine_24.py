"""Piloswine (ME2 24 -- JP M2 024; English PFL/24). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="eaca1f78-cdf9-5d45-810c-77b43248197c",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    display_name="Piloswine",
    searchable_by=["Piloswine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
        Attack(
            title="Frost Smash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
