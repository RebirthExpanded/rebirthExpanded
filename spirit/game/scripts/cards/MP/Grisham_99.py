"""Grisham (JP MEGA Promo 099 -- no English print yet).

Supporter.

  "Heal 50 damage from all Pokemon in play (both yours and your opponent's)."
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef


async def grisham(ctx):
    for pokemon in list(ctx.my_pokemon_in_play()) + list(ctx.opponent_pokemon_in_play()):
        await ctx.heal(50, pokemon)


card = SupporterCardDef(
    guid="43e8e402-3667-5af3-9da4-0e7e7b879dbb",
    key="MP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grisham.Name",
    display_name="Grisham",
    searchable_by=["Grisham", "Supporter", "Grisham"],
    subtypes=["Supporter"],
    collector_number=99,
    set_code="MP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    effect=grisham,
)
