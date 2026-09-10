from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _caitlin_playable(board, player_id, card=None):
    """A card in hand besides this Caitlin.

    "Put any number of cards from your hand on the bottom of your deck in
    any order. THEN, draw that many cards." Cards go under the deck without
    a shuffle, so with an empty hand there is nothing to put, nothing to
    draw, and nothing at all -- unlike Bruno or Kabu, which shuffle the deck
    on the way and so keep their "Then" alive.
    """
    hand = board.find_player_area(player_id, "hand")
    return any(c is not card for c in (hand.children if hand else []))


async def caitlin(ctx):
    """Put any number of hand cards on the bottom of the deck in any order,
    then draw that many cards."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, len(hand), minimum=0, ordered=True,
        prompt="Choose any number of cards to put on the bottom of your deck, in order.",
    )
    if not picks:
        return
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(len(picks))


card = SupporterCardDef(
    guid="4a09afb2-c434-55ac-a2d7-4bd366e0ded5",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caitlin.Name",
    display_name="Caitlin",
    searchable_by=["Caitlin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=caitlin,
    condition=_caitlin_playable,
)
