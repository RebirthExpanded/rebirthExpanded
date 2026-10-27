"""Harlequin (RSV10PT5 83 -- JP SV11W 083; English WHT/163, WHT/83). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def harlequin(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        hand = list(ctx.hand(pid))
        if hand:
            await ctx.shuffle_into_deck(hand, pid)
        else:
            await ctx.shuffle_deck(pid)
    results = await ctx.flip_coins(1, "Harlequin")
    mine, theirs = (5, 3) if results and results[0] else (3, 5)
    await ctx.draw_cards(mine)
    await ctx.draw_cards(theirs, player_id=ctx.opponent_id)


card = SupporterCardDef(
    guid="efc0fa32-e557-520e-86de-0e574f856b3d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Harlequin.Name",
    display_name="Harlequin",
    searchable_by=["Harlequin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=harlequin,
)
