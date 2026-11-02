"""Lebanne (MP1 171 -- JP MP 171; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def _lebanne(ctx):
    """Flip a coin: heal 150 from your Active on heads, 30 on tails."""
    results = await ctx.flip_coins(1, "Lebanne")
    await ctx.heal(150 if results and results[0] else 30, ctx.my_active())


card = SupporterCardDef(
    guid="488cae0f-8d4c-5e9e-94a6-392acb21703b",
    key="MP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lebanne.Name",
    display_name="Lebanne",
    searchable_by=["Lebanne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="MP1",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    effect=_lebanne,
)
