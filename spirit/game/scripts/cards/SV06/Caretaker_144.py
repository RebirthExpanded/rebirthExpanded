"""Caretaker (SV06 144 -- JP SV5a 061; English TWM/144, TWM/203). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


async def caretaker(ctx):
    drawn = await ctx.draw_cards(2)
    stadium = ctx.stadium_in_play()
    if drawn and stadium is not None and getattr(def_for(stadium.archetype_id), "display_name", "") == "Community Center":
        await ctx.shuffle_into_deck([ctx.source], ctx.player_id)


card = SupporterCardDef(
    guid="ade823a8-0f85-5815-9ca4-65ae5c0bc449",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caretaker.Name",
    display_name="Caretaker",
    searchable_by=["Caretaker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=caretaker,
)
