"""Pidgeot ex (SV - Obsidian Flames 164/197).

Stage 2 Colorless Pokemon ex. HP 280, weakness Lightning x2, resistance
Fighting -30, no retreat cost.

  Ability  Quick Search  Once during your turn, you may search your deck
                         for a card and put it into your hand. Then,
                         shuffle your deck. You can't use more than 1
                         Quick Search Ability each turn.

  Blustery Wind [CC] 120  You may discard a Stadium in play.

The last sentence is shared_once_per_turn, not the ordinary per-entity
limit: two Pidgeot ex in play still give you one search between them.

The Ability carries a condition of its own for the same reason Computer
Search is not offered on an empty deck -- an Ability that can do nothing
may not be used. The engine's empty-deck gate covers Trainer cards played
from hand, which this is not, so the card asks for itself.

The pool's first Obsidian Flames card, so SV3 is registered here (OBF,
sorted between SV2 and SV4), the way SV4 was for Technical Machine:
Evolution.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

QUICK_SEARCH = "Quick Search"


def _deck_not_empty(board, player_id, pokemon):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def quick_search(ctx):
    """Search your deck for any 1 card, put it into your hand, shuffle."""
    picks = await ctx.search_deck(
        count=1, minimum=1,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def blustery_wind(ctx):
    """120. You may discard a Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="52b99afd-2623-5d49-95d5-f47bee08949d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotex.Name",
    display_name="Pidgeot ex",
    searchable_by=["Pidgeot ex", "Stage 2", "ex", "Pidgeotex"],
    subtypes=["Stage 2", "ex"],
    collector_number=164,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Ability(
            title=QUICK_SEARCH,
            game_text=(
                "Once during your turn, you may search your deck for a card "
                "and put it into your hand. Then, shuffle your deck. You "
                "can't use more than 1 Quick Search Ability each turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn=QUICK_SEARCH,
            condition=_deck_not_empty,
            effect=quick_search,
        ),
        Attack(
            title="Blustery Wind",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=blustery_wind,
        ),
    ],
)
