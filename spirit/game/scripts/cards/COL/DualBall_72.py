"""Dual Ball (HGSS - Call of Legends 72/95 -- JP El 010/015, the art here).

Item.

  "Flip 2 coins. For each heads, search your deck for a Basic Pokemon,
   reveal it, and put it into your hand. Then, shuffle your deck."

Two heads search for two, one heads for one, two tails for none. The
low-resolution art is all pokemon-card.com carries for this print.
"""

from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.data_utils import ItemCardDef


async def dual_ball(ctx):
    heads = sum(1 for flip in await ctx.flip_coins(2, "Dual Ball") if flip)
    if not heads:
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=heads, minimum=0,
        prompt=f"Choose up to {heads} Basic Pokémon to put into your hand.")
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="010260a0-42be-5d81-87c1-308e97398550",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item", "DualBall"],
    subtypes=["Item"],
    collector_number=72,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=dual_ball,
)
