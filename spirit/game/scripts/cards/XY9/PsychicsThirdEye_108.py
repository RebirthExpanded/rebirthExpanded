"""Psychic's Third Eye (XY - BREAKpoint 108/122 -- JP XY9-B 078/080, the art here).

Supporter.

  "Your opponent reveals his or her hand. Discard as many cards as you
   like from your hand. Then, draw that many cards."

The reveal shows their hand to the user only; the discard is any number
(0 is fine), and the draw matches what was discarded.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


async def psychics_third_eye(ctx):
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    hand = list(ctx.hand())
    if not hand:
        return
    discarded = await ctx.discard_from_hand(
        len(hand), minimum=0, prompt="Discard as many cards as you like")
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
