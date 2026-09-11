"""Magcargo (SM - Celestial Storm 24/168 -- JP SM6b 007/066).

Stage 1 Fire Pokemon, evolves from Slugma. HP 90, weakness Water x2,
retreat 3.

  Ability  Smooth Over  Once during your turn (before your attack), you may
                        search your deck for a card, shuffle your deck, then
                        put that card on top of it.
  Combustion  [RCC] 50

Any card, and the shuffle comes BEFORE the card goes on top, so it is
guaranteed to be the next draw.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)


async def smooth_over(ctx):
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put on top of your deck.")
    await ctx.shuffle_deck()
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


def _deck_not_empty(board, player_id, pokemon) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


card = PokemonCardDef(
    guid="6f2364ae-ae1b-546e-b5bd-a7b4cff61d9d",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Smooth Over",
            game_text="Once during your turn (before your attack), you may search your deck for a card, shuffle your deck, then put that card on top of it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=smooth_over,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
