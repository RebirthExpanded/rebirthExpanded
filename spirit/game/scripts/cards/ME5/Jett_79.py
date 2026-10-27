"""Jett (ME5 79 -- JP MP 075; English PBL/79). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


async def jett(ctx):
    n = sum(1 for p in ctx.opponent_pokemon_in_play() if "SV_Mega" in (subtypes_for(p.archetype_id) or []))
    if n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="4237e580-c325-59c8-837e-207b3ca5cfb6",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jett.Name",
    display_name="Jett",
    searchable_by=["Jett", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=jett,
)
