"""Pokemon Communication (SM - Team Up 152/181 -- JP SM9 082/095).

Item.

  "Reveal a Pokemon from your hand and put it into your deck. If you do,
   search your deck for a Pokemon, reveal it, and put it into your hand.
   Then, shuffle your deck."

A trade, not a search: the deck gives one Pokemon and takes one back.

Two rules meet here and both cut the usual way round.

"If you do" is the chain rule this pool already applies everywhere: with
no Pokemon in hand the first half cannot happen, so the second half cannot
either and the card is unplayable. That is the condition.

The empty-deck gate is the opposite case, and this is the first card in
the pool it gets wrong. legal_actions refuses a deck search when the deck
is empty, on the reading that no card puts cards INTO the deck before
searching it -- this one does, so with an empty deck the search still has
exactly one card to find: the Pokemon just traded in. The definition
overrules the automatic reading with searches_deck = False, which is the
escape hatch data_utils.searches_deck documents.

"Into your deck" and not "on top of your deck" -- the BW-era print put it
on top, this one buries it and the shuffle at the end settles where.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_pokemon_card


def _hand_pokemon(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return [c for c in (hand.children if hand else []) if is_pokemon_card(c)]


def _communication_playable(board, player_id, card=None):
    """"If you do": no Pokemon in hand, nothing to trade, nothing to find."""
    return bool(_hand_pokemon(board, player_id))


async def pokemon_communication(ctx):
    """Trade a Pokemon from hand into the deck for one out of it."""
    candidates = _hand_pokemon(ctx.board, ctx.player_id)
    if not candidates:
        return
    given = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Pokémon to put into your deck.")
    if not given:
        return
    await ctx.reveal_cards(given)
    # "put it into your deck": anywhere in it, and the printed shuffle at the
    # end settles where -- shuffle_into_deck is that move and that shuffle.
    await ctx.shuffle_into_deck(given)
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=1,
        prompt="Choose a Pokémon to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ae4a2261-afb9-5a4b-99ad-963af08e2a47",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCommunication.Name",
    display_name="Pokémon Communication",
    searchable_by=["Pokémon Communication", "Pokemon Communication", "Item",
                   "PokemonCommunication"],
    subtypes=["Item"],
    collector_number=152,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=pokemon_communication,
    condition=_communication_playable,
)

# The deck is never empty at the moment this card searches -- it just put a
# Pokemon in -- so the automatic empty-deck gate must not speak for it.
card.searches_deck = False
