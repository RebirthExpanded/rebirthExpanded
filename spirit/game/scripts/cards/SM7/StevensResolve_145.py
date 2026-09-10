"""Steven's Resolve (SM - Celestial Storm 145/168).

Supporter.

  "Search your deck for up to 3 cards and put them into your hand. Then,
   shuffle your deck. Your turn ends."

Any 3 cards at all -- the search has no filter, which is what makes ending
the turn its price. ctx.ends_turn carries that, the way Boost Shake does.

The deck-search gate keeps it off the table with an empty deck; with one
or two cards left it takes what there is.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def stevens_resolve(ctx):
    """Any 3 cards out of the deck, and then the turn is over."""
    picks = await ctx.search_deck(
        count=3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()
    ctx.ends_turn = True


card = SupporterCardDef(
    guid="375fcfe2-8a81-5894-99d0-f7b0d055421b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter", "StevensResolve"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    effect=stevens_resolve,
)
