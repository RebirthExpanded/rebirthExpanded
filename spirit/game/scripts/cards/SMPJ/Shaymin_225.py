"""Shaymin (SMPJ 225 -- JP SMP 225; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card

from spirit.game.session.ai_player import AIPlayer


def _gratitude_condition(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return board.active_pokemon(player_id) is pokemon and bool(deck and deck.children)


async def sign_of_gratitude(ctx):
    """Draw a card. Your opponent may draw a card."""
    await ctx.draw_cards(1)
    if not ctx.deck_top(1, player_id=ctx.opponent_id):
        return
    if isinstance(ctx.session.players.get(ctx.opponent_id), AIPlayer):
        wants = True
    else:
        wants = await ctx.choose("Your opponent's Shaymin used Sign of Gratitude. Draw a card?", ["Draw", "Don't draw"],
                                 player_id=ctx.opponent_id, use_panel=False) == 0
    if wants:
        await ctx.draw_cards(1, ctx.opponent_id)


async def _energy_flare(ctx):
    """Attach up to 2 basic Energy cards from your hand to 1 of your Benched Pokemon."""
    bench = ctx.my_bench()
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(energies, 2, minimum=0, prompt="Choose up to 2 basic Energy cards to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach Energy to")
    if target is not None:
        for card in picks:
            await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="d421cdf8-79f8-5b99-9dfb-bd3d60d80dcc",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic"],
    subtypes=["Basic"],
    collector_number=225,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Ability(
            title="Sign of Gratitude",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may draw a card. If you do, your opponent may draw a card.",
            activation=Activations.ONCE_PER_TURN,
            condition=_gratitude_condition,
            effect=sign_of_gratitude,
        ),
        Attack(
            title="Energy Flare",
            game_text="Attach up to 2 basic Energy cards from your hand to 1 of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_energy_flare,
        ),
    ],
)
