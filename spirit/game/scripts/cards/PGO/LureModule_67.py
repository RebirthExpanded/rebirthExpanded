from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def _lure_module_playable(board, player_id, card=None):
    """At least one deck with a card in it.

    "Each player reveals the top 3 cards of their deck ... THEN, each player
    shuffles the other cards back into their deck." Each player's half runs
    on their own deck, so one deck with cards left is enough for the card to
    do something; only two empty decks kill it outright.
    """
    for pid in board.player_ids:
        deck = board.find_player_area(pid, "deck")
        if deck and deck.children:
            return True
    return False


async def lure_module_effect(ctx):
    """Each player reveals the top 3 of their deck; Pokemon found go to hand,
    the rest is shuffled back."""
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(3, player_id=pid)
        if not top:
            continue
        await ctx.reveal_cards(top)
        matches = [c for c in top if is_pokemon_card(c)]
        if matches:
            await ctx.put_in_hand(matches, reveal=False)
        await ctx.shuffle_deck(player_id=pid)


card = ItemCardDef(
    guid="d17d2b10-6400-5d79-9ae6-63504e64447f",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureModule.Name",
    display_name="Lure Module",
    searchable_by=["Lure Module", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    effect=lure_module_effect,
    condition=_lure_module_playable,
)
