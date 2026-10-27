"""Dangerous Laser (SV065 58 -- JP SV6a 054; English SFA/58). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.attributes import SpecialConditions


async def dangerous_laser(ctx):
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.BURNED)
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = ItemCardDef(
    guid="8bb3e957-51c4-5112-8e76-98da7a654d0d",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousLaser.Name",
    display_name="Dangerous Laser",
    searchable_by=["Dangerous Laser", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=58,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=dangerous_laser,
)
