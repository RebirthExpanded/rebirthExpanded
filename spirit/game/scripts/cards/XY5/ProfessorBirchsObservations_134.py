"""Professor Birch's Observations (XY - Primal Clash 134/160 -- JP XY5 067/070,
the art here).

Supporter.

  "Shuffle your hand into your deck. Then, flip a coin. If heads, draw 7
   cards. If tails, draw 4 cards."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

HEADS_DRAW = 7
TAILS_DRAW = 4


async def professor_birchs_observations(ctx):
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    heads = (await ctx.flip_coins(1, "Professor Birch's Observations"))[0]
    await ctx.draw_cards(HEADS_DRAW if heads else TAILS_DRAW)


card = SupporterCardDef(
    guid="04705c0e-6212-5623-8941-c33becd90a1e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirchsObservations.Name",
    display_name="Professor Birch's Observations",
    searchable_by=["Professor Birch's Observations", "Supporter",
                   "ProfessorBirchsObservations"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=professor_birchs_observations,
)
