"""Lumiose Galette (ME3 78 -- JP M3 071; English POR/78). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.attributes import SpecialConditions


async def lumiose_galette(ctx):
    active = ctx.my_active()
    if active is None:
        return
    await ctx.heal(20, active)
    have = list(active.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    conds = [c for c in SpecialConditions if CLIENT_SPECIAL_CONDITION_NAMES.get(c) in have]
    if not conds:
        return
    index = 0
    if len(conds) > 1:
        index = await ctx.choose("Choose a Special Condition to remove",
                                 [CLIENT_SPECIAL_CONDITION_NAMES[c] for c in conds])
    await ctx.cure_condition(active, conds[index])


card = ItemCardDef(
    guid="62973567-b652-5660-a1dc-d82f72f5e118",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumioseGalette.Name",
    display_name="Lumiose Galette",
    searchable_by=["Lumiose Galette", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=lumiose_galette,
)
