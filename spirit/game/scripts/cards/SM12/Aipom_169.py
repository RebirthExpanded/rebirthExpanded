"""Aipom (SM - Cosmic Eclipse 169/236 -- JP SM12 075/095).

Basic Colorless Pokemon. HP 60, weakness Fighting x2, retreat 1.

  Ability  Scampering Tail  Once during your turn (before your attack), you
                            may put the top card of your opponent's deck on
                            the bottom of their deck without looking at it.
  Tail Smack  [CC] 20

Not offered against an empty deck.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef


def _opponent_deck_not_empty(board, player_id, pokemon) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    deck = board.find_player_area(opponent, "deck") if opponent else None
    return bool(deck and deck.children)


async def scampering_tail(ctx):
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    if deck is None or not deck.children:
        return
    await ctx.put_on_bottom_of_deck(deck.children[-1])


card = PokemonCardDef(
    guid="65ca20e2-34cb-540f-973f-5fa9ba0448e9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=['Aipom', 'Basic', 'Aipom'],
    subtypes=['Basic'],
    collector_number=169,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Ability(
            title="Scampering Tail",
            game_text="Once during your turn (before your attack), you may put the top card of your opponent's deck on the bottom of their deck without looking at it.",
            activation=Activations.ONCE_PER_TURN,
            condition=_opponent_deck_not_empty,
            effect=scampering_tail,
        ),
        Attack(title="Tail Smack", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
