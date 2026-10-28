"""Oricorio (SV2 33 -- JP SV1a 016; English PAF/113, PAL/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10

from spirit.game.session.effects import is_evolution_pokemon


def _ardent_condition(board, player_id, pokemon) -> bool:
    a = board.active_pokemon(player_id)
    return a is not None and is_evolution_pokemon(a) and _counters(board, a) > 0


async def ardent_dancing(ctx):
    a = ctx.board.active_pokemon(ctx.player_id)
    if a is not None and is_evolution_pokemon(a):
        await ctx.heal(20, a)


card = PokemonCardDef(
    guid="3afaa312-6e03-503f-9589-3b4d01a71682",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=741,
    abilities=[
        Ability(
            title="Ardent Dancing",
            game_text="Once during your turn, you may heal 20 damage from your Active Evolution Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_ardent_condition,
            effect=ardent_dancing,
        ),
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
