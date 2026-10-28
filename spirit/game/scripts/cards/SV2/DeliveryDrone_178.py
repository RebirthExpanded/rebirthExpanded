"""Delivery Drone (SV2 178 -- JP SV2D 066; English PAL/178). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

async def delivery_drone(ctx):
    results = await ctx.flip_coins(2, "Delivery Drone")
    if results and all(results):
        picks = await ctx.search_deck(count=1, minimum=0, prompt="Choose a card to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
        await ctx.shuffle_deck()


card = ItemCardDef(
    guid="7cb0df6d-950f-5805-9f1a-772bcdb0df0d",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeliveryDrone.Name",
    display_name="Delivery Drone",
    searchable_by=["Delivery Drone", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=delivery_drone,
)
