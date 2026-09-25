"""Timer Ball (SM - Sun & Moon 134/149 -- JP SM1S 054/060).

Item.

  "Flip 2 coins. For each heads, search your deck for an Evolution
   Pokemon, reveal it, and put it into your hand. Then, shuffle your deck."

Two tails: no search, so the deck is not opened or shuffled.
"""

from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.data_utils import ItemCardDef


async def timer_ball(ctx):
    heads = sum(1 for h in await ctx.flip_coins(2, "Timer Ball") if h)
    if heads <= 0:
        return
    picks = await ctx.search_deck(
        is_evolution_pokemon, count=heads, minimum=0,
        prompt=f"Choose up to {heads} Evolution Pokémon.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="32764300-84fb-5e8c-ac4f-511b56f587de",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimerBall.Name",
    display_name="Timer Ball",
    searchable_by=["Timer Ball", "Item", "TimerBall"],
    subtypes=["Item"],
    collector_number=134,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=timer_ball,
)
