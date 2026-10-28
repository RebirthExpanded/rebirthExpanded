"""Magikarp (SV2 42 -- JP SV1a 022; English PAL/203, PAL/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="04b84b7b-7909-5c58-aa15-aa4569dd8f97",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Expert Splasher",
            game_text="Flip 2 coins. If both of them are heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus=20, require_all=True),
        ),
    ],
)
