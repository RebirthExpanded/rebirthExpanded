"""Falkner (SV2 180 -- JP SV1a 068; English PAL/180, PAL/251). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def falkner(ctx):
    await ctx.draw_cards(2)
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == ctx.player_id:
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="b1695598-f104-5c64-a677-c209192e7571",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Falkner.Name",
    display_name="Falkner",
    searchable_by=["Falkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=falkner,
)
