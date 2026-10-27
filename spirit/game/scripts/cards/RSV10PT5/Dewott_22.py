"""Dewott (RSV10PT5 22 -- JP SV11W 019; English WHT/106, WHT/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="716242b9-1834-5624-a0cf-326ddab5b805",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    display_name="Dewott",
    searchable_by=["Dewott", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    family_id=501,
    abilities=[
        Attack(
            title="Energized Shell",
            game_text="This attack does 30 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self"), 30),
        ),
    ],
)
