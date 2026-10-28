"""Wiglett (SV4 51 -- JP SV4K 023; English PAR/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="2ab09649-a761-516f-9f43-df97fc3767b9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Fury Headbutt",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(coins=3, per_heads=10),
        ),
    ],
)
