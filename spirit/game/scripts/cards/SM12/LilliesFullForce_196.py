"""Lillie's Full Force (SM - Cosmic Eclipse 196/236 -- JP SM11b 049/049).

Supporter.

  "Draw 4 cards. At the end of this turn, if you have 3 or more cards in
   your hand, shuffle cards from your hand into your deck until you have 2
   cards in your hand."

The end-of-turn half is left with ctx.at_end_of_this_turn, so it is
ordered with the end-of-turn Abilities: with Togekiss's Precious Gift also
due, the turn player -- Togekiss's owner -- picks which comes first.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

TITLE = "Lillie's Full Force"


def _three_or_more(ctx) -> bool:
    return len(ctx.hand()) >= 3


async def _down_to_two(ctx):
    hand = list(ctx.hand())
    extra = len(hand) - 2
    if extra <= 0:
        return
    picks = await ctx.choose_cards(
        hand, extra, minimum=extra,
        prompt=f"Choose {extra} card(s) to shuffle into your deck (keep 2).")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


async def lillies_full_force(ctx):
    await ctx.draw_cards(4)
    ctx.at_end_of_this_turn(TITLE, _down_to_two, applies=_three_or_more)


card = SupporterCardDef(
    guid="a558f30a-7b29-543b-babe-006b797cc8a8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesFullForce.Name",
    display_name="Lillie's Full Force",
    searchable_by=["Lillie's Full Force", "Supporter", "LilliesFullForce"],
    subtypes=["Supporter"],
    collector_number=196,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=lillies_full_force,
)
