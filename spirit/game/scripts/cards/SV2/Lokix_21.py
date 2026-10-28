"""Lokix (SV2 21 -- JP SV1a 010; English PAL/21). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _evolved_this_turn(ctx) -> bool:
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


card = PokemonCardDef(
    guid="38a4bd3b-9343-5578-9efd-2e10ee2131c6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Assaulting Kick",
            game_text="If this Pokémon evolved from Nymble during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_this_turn, 100),
        ),
        Attack(
            title="Speed Attack",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
