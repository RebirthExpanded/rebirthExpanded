"""Norman (SV4 168 -- JP SV4K 065; English PAR/168, PAR/237). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


async def norman(ctx):
    await ctx.draw_cards(2)
    d = ctx.board.active_pokemon(ctx.opponent_id)
    if d is not None and "ex" in (subtypes_for(d.archetype_id) or []):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="16452ca9-9db9-5925-8846-3e25ca45bd74",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Norman.Name",
    display_name="Norman",
    searchable_by=["Norman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=norman,
)
