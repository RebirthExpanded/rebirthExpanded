"""Roark (SV4 173 -- JP SV4M 064; English PAR/173, PAR/242). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.card_effects.trainers import is_basic_energy_card


async def roark(ctx):
    await ctx.draw_cards(2)
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card")
        if picks:
            await ctx.put_in_hand(picks)


card = SupporterCardDef(
    guid="4ba23d4b-12a1-5106-adf7-3ed6f0cb3046",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roark.Name",
    display_name="Roark",
    searchable_by=["Roark", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=roark,
)
