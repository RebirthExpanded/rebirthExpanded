"""Hiker (SM - Celestial Storm 133/168 -- JP SM-P 107, the art here).

Supporter.

  "Look at the top 5 cards of your deck or your opponent's deck and
   choose 1 of them. Shuffle the other cards back into that deck. Then,
   put the card you chose on top of that deck."

Whose deck is a "Choose 1" on the card; the look is private to the
player (the deck browser, not a reveal), and the shuffle goes first so
the chosen card lands on top of a fresh order (Magcargo's Smooth Over).
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

LOOK = 5


async def hiker(ctx):
    which = await ctx.choose(
        "Whose deck?", ["Your deck", "Your opponent's deck"],
        descriptions=["Look at the top 5 cards of your deck.",
                      "Look at the top 5 cards of your opponent's deck."])
    pid = ctx.player_id if which == 0 else ctx.opponent_id
    top = ctx.deck_top(LOOK, player_id=pid)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1, prompt="Choose a card to put on top of that deck.")
    await ctx.shuffle_deck(pid)
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = SupporterCardDef(
    guid="57d0c882-882d-52db-96d2-e0d55416548b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=hiker,
)
