"""Computer Search (BW - Boundaries Crossed 137/149).

Item, ACE SPEC.

  "Discard 2 cards from your hand. (If you can't discard 2 cards, you can't
   play this card.) Search your deck for a card and put it into your hand.
   Shuffle your deck afterward."

Ultra Ball's shape with the filter taken off: the same 2-card cost, the
same condition (hand_size_at_least(3), the parenthesis spelled out), and
a search whose predicate is None, so every card in the deck is selectable.

Two things follow from the text that Ultra Ball does not share:

  - No reveal. Ultra Ball says "reveal it, and put it into your hand";
    this one just puts it there, so put_in_hand takes reveal=False.
  - The search is mandatory, not "up to 1" -- minimum=1. There is nothing
    to whiff on when any card matches, and an empty deck is handled by
    choose_cards, which returns nothing rather than prompting.

The discard is a COST paid before the deck opens, which search_deck's
choreography flush now guarantees on screen as well as in the board state.

The ACE SPEC deck limit is enforced in game/rules.py; BW7 came into
Expanded with Town Map.
"""

from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def computer_search(ctx):
    """Discard 2 other cards, then take any 1 card out of the deck."""
    if len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Computer Search")) < 2:
        return
    picks = await ctx.search_deck(
        count=1, minimum=1,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="376fcbde-ec7e-56d2-8f3c-ae2788f8d0ca",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search", "Item", "ACE SPEC", "ComputerSearch"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=137,
    set_code="BW7",
    rarity=Rarities.Ace,
    effect=computer_search,
    condition=hand_size_at_least(3),
)
