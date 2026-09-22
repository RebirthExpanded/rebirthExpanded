"""Ilima (SM - Sun & Moon 121/149 -- JP SM1S 058/060, the art here).

Supporter.

  "Each player shuffles their hand into their deck. Then, each player
   flips a coin. If heads, that player draws 6 cards. If tails, that
   player draws 3 cards."

Both hands go first, then the two flips: a player whose own flip decides
their draw, so the coins are thrown one after the other and each player
sees their own result.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

HEADS_DRAW = 6
TAILS_DRAW = 3


async def ilima(ctx):
    for player_id in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(player_id), player_id)
    for player_id in (ctx.player_id, ctx.opponent_id):
        heads = (await ctx.flip_coins(1, "Ilima", flipper_id=player_id))[0]
        await ctx.draw_cards(HEADS_DRAW if heads else TAILS_DRAW, player_id=player_id)


card = SupporterCardDef(
    guid="8fa5fd8d-8f06-5b78-99e5-5cf0daa7326d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ilima.Name",
    display_name="Ilima",
    searchable_by=["Ilima", "Supporter"],
    subtypes=["Supporter"],
    collector_number=121,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=ilima,
)
