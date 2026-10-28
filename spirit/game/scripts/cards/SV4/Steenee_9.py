"""Steenee (SV4 9 -- JP SV4K 007; English PAR/9). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c75a3233-810a-5db2-bb4c-4afa4317481a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    display_name="Steenee",
    searchable_by=["Steenee", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 40 damage for each heads.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(coins=2, per_heads=40),
        ),
    ],
)
