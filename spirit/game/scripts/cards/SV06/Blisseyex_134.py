"""Blissey ex (SV06 134 -- JP SV6 085; English TWM/134, TWM/201). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def _maybe_draw_to_6(ctx):
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


def _happy_switch_condition(board, player_id, pokemon) -> bool:
    mine = board.pokemon_in_play(player_id)
    return len(mine) >= 2 and any(is_basic_energy_card(c) for p in mine for c in p.children)


async def happy_switch(ctx):
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=is_basic_energy_card, max_count=1,
                                 prompt="Choose a Basic Energy to move")


async def return_(ctx):
    await ctx.deal_damage()
    await _maybe_draw_to_6(ctx)


card = PokemonCardDef(
    guid="691a7956-cf97-5bca-af46-14b190cfff22",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blisseyex.Name",
    display_name="Blissey ex",
    searchable_by=["Blissey ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=134,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=440,
    abilities=[
        Ability(
            title="Happy Switch",
            game_text="Once during your turn, you may move a Basic Energy from 1 of your Pokémon to another of your Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_happy_switch_condition,
            effect=happy_switch,
        ),
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=return_,
        ),
    ],
)
