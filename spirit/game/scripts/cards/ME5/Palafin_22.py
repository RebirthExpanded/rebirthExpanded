"""Palafin (ME5 22 -- JP M5 021; English PBL/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _one_left(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) == 1


card = PokemonCardDef(
    guid="dee98592-7e15-50b9-8050-43ceb4d3427c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Knuckle Justice",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_one_left, 200),
        ),
    ],
)
