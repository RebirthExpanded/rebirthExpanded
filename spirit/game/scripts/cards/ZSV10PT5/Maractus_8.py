"""Maractus (ZSV10PT5 8 -- JP SV11B 008; English BLK/8, BLK/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _healed_this_turn(ctx) -> bool:
    return ctx.attacker.entity_id in ctx.session.turn_state.healed_entities


card = PokemonCardDef(
    guid="656e69f4-8753-5a01-9f0d-dd2c3b1b7985",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Lively Needles",
            game_text="If this Pokémon was healed during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_healed_this_turn, 100),
        ),
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
