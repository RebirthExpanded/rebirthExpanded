"""Deduction Kit (SV08 171 -- JP SV8 094; English SSP/171). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

async def deduction_kit(ctx):
    top = list(ctx.deck_top(3))
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Shuffle them and put them on the bottom of your deck? (No: put them back in any order)"):
        import random
        random.shuffle(top)
        for card in top:
            await ctx.put_on_bottom_of_deck(card)
    else:
        await ctx.reorder_deck_top(len(top))


card = ItemCardDef(
    guid="8f11c828-9b92-5d36-8044-2ac65e01d8b3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeductionKit.Name",
    display_name="Deduction Kit",
    searchable_by=["Deduction Kit", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=deduction_kit,
)
