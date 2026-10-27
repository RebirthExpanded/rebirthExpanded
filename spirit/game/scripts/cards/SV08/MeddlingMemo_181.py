"""Meddling Memo (SV08 181 -- JP SV7a 055; English SSP/181). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

async def meddling_memo(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    import random
    random.shuffle(hand)
    for card in hand:
        await ctx.put_on_bottom_of_deck(card)
    await ctx.draw_cards(len(hand), player_id=ctx.opponent_id)


card = ItemCardDef(
    guid="356f17b8-af37-5d91-af8f-9e113c4c2725",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeddlingMemo.Name",
    display_name="Meddling Memo",
    searchable_by=["Meddling Memo", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=meddling_memo,
)
