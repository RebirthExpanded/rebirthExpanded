"""Psychic's Third Eye (XY - BREAKpoint 108/122 -- JP XY9-B 078/080, the art here).

Supporter.

  "Your opponent reveals his or her hand. Discard as many cards as you
   like from your hand. Then, draw that many cards."

The reveal shows their hand to the user only. "As many as you like" is
at least 1 while any other card is in hand (official ruling); the draw
matches what was discarded.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


async def psychics_third_eye(ctx):
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    # The Supporter itself is still in hand while it resolves: not a pick.
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if not hand:
        return
    discarded = await ctx.discard_from_hand(
        len(hand), minimum=1, exclude=[ctx.source],
        prompt="Discard as many cards as you like (at least 1)")
    if discarded:
        await ctx.draw_cards(len(discarded))


card = SupporterCardDef(
    guid="4b63e586-ad26-5030-8664-36d124eb2b46",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicsThirdEye.Name",
    display_name="Psychic's Third Eye",
    searchable_by=["Psychic's Third Eye", "Supporter", "PsychicsThirdEye"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=psychics_third_eye,
)
