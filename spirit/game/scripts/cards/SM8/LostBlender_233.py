"""Lost Blender (SM - Lost Thunder 181/214 -- JP SM8 083/095, the art here).

Item.

  "Put 2 cards from your hand in the Lost Zone. Then, draw a card.
   (If you can't put 2 cards from your hand in the Lost Zone, you can't
   play this card.)"

The hand must hold 2 other cards (3 counting the Blender itself); both
go to the Lost Zone before the draw.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least
from spirit.game.data_utils import ItemCardDef

COST = 2


async def lost_blender(ctx):
    hand = ctx.hand()
    if len(hand) < COST:
        return
    picks = await ctx.choose_cards(
        hand, COST, minimum=COST, prompt="Choose 2 cards to put in the Lost Zone")
    if len(picks) < COST:
        return
    await ctx.move_to_lost_zone(picks)
    await ctx.draw_cards(1)


card = ItemCardDef(
    guid="b7c65064-dd78-5aa1-8e7b-2a0ce0dc14cc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostBlender.Name",
    display_name="Lost Blender",
    searchable_by=["Lost Blender", "Item", "LostBlender"],
    subtypes=["Item"],
    collector_number=233,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    condition=hand_size_at_least(COST + 1),
    effect=lost_blender,
)
