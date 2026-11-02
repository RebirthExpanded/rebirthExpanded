"""Professor Burnet (Promo_SWSH 167 -- JP SP5 013; English SP/167). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import SupporterCardDef


async def _professor_burnet(ctx):
    picks = await ctx.search_deck(None, 2, minimum=0, prompt="Choose up to 2 cards to discard.")
    if picks:
        await ctx.discard_cards(picks)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="0572d151-8fd8-5efb-85b9-b5effac55525",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBurnet.Name",
    display_name="Professor Burnet",
    searchable_by=["Professor Burnet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    effect=_professor_burnet,
    condition=su.requires_deck(),
)
