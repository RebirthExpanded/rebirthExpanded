"""Swadloon (RSV10PT5 2 -- JP SV11W 002; English WHT/2, WHT/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _active_damaged(board, player_id, pokemon) -> bool:
    active = board.active_pokemon(player_id)
    return active is not None and _counters(board, active) > 0


async def healing_leaves(ctx):
    active = ctx.board.active_pokemon(ctx.player_id)
    if active is not None:
        await ctx.heal(20, active)


card = PokemonCardDef(
    guid="38ec1370-2b75-5d0d-837a-c954350c26e7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    display_name="Swadloon",
    searchable_by=["Swadloon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    family_id=540,
    abilities=[
        Ability(
            title="Healing Leaves",
            game_text="Once during your turn, you may heal 20 damage from your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_active_damaged,
            effect=healing_leaves,
        ),
        Attack(
            title="Bug Buzz",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
