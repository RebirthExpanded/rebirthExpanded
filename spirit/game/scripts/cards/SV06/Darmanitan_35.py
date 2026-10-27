"""Darmanitan (SV06 35 -- JP SV6 018; English TWM/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9a919ac1-fc52-5fdf-b1ea-183c2755a160",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=60,
        ),
        Attack(
            title="Inferno Onrush",
            game_text="This Pokémon also does 70 damage to itself.",
            cost={PokemonTypes.FIRE: 3},
            damage=210,
            effect=ac.recoil_attack(70),
        ),
    ],
)
