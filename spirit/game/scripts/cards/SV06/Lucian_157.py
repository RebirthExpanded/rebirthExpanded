"""Lucian (SV - Twilight Masquerade 157/167 -- JP SV5a 062/066, the art here).

Supporter.

  "Each player shuffles their hand and puts it on the bottom of their
   deck. Then, each player flips a coin. If heads, that player draws 6
   cards. If tails, that player draws 3 cards."

Ilima with Marnie's disposal: the hands go UNDER the decks rather than
into them, so a shuffled deck keeps its order above them.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

HEADS_DRAW = 6
TAILS_DRAW = 3


async def lucian(ctx):
    for player_id in (ctx.player_id, ctx.opponent_id):
        await ctx.hand_to_bottom_of_deck(player_id)
    for player_id in (ctx.player_id, ctx.opponent_id):
        heads = (await ctx.flip_coins(1, "Lucian", flipper_id=player_id))[0]
        await ctx.draw_cards(HEADS_DRAW if heads else TAILS_DRAW, player_id=player_id)


card = SupporterCardDef(
    guid="80c23ae1-c345-5a2c-944b-e6b760899372",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lucian.Name",
    display_name="Lucian",
    searchable_by=["Lucian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=lucian,
)
