"""Lacey (SV085 114 -- JP SV7 098; English PRE/114, PRE/175, SCR/139, SCR/166, SCR/172). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects import attacks_common as ac


async def lacey(ctx):
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.player_id)
    else:
        await ctx.shuffle_deck()
    await ctx.draw_cards(8 if ac.count_prizes_remaining("opponent")(ctx) <= 3 else 4)


card = SupporterCardDef(
    guid="eb728c5a-dbf2-587b-a963-d2174c4a391f",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lacey.Name",
    display_name="Lacey",
    searchable_by=["Lacey", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=lacey,
)
