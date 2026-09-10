"""Stadium Nav (SM - Unified Minds 208/236 -- JP SM11 082/094).

Item.

  "Flip 2 coins. For each heads, search your deck for a Stadium card,
   reveal it, and put it into your hand. Then, shuffle your deck."

The flip decides how many, so it happens before the deck opens and the
search asks for that many at once rather than once per heads -- two heads
is "up to 2 Stadium cards", not two separate one-card searches, which
matters only in that the player sees one list.

Tails twice still shuffles: the deck was searched for zero cards, which
is the printed "then". The empty-deck gate in legal_actions keeps the card
off the panel with no deck at all, so the flip is never spent on nothing.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_stadium_card

TITLE = "Stadium Nav"


async def stadium_nav(ctx):
    """Flip 2 coins; one Stadium out of the deck per heads."""
    heads = sum(1 for flip in await ctx.flip_coins(2, TITLE) if flip)
    if heads:
        picks = await ctx.search_deck(
            is_stadium_card, count=heads, minimum=0,
            prompt="Choose a Stadium card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="b3c4bc23-d219-5c26-b842-cb0c57972ecf",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StadiumNav.Name",
    display_name=TITLE,
    searchable_by=["Stadium Nav", "Item", "StadiumNav"],
    subtypes=["Item"],
    collector_number=208,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=stadium_nav,
)
