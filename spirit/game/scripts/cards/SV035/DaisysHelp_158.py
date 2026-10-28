"""Daisy's Help (SV035 158 -- JP SV2a 163; English MEW/158, MEW/195). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

async def daisys_help(ctx):
    await ctx.draw_cards(2)
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = [c for c in (area.children if area else []) if not c.face_up]
    if prizes:
        await ctx.reveal_cards(prizes, to_player=ctx.player_id)


card = SupporterCardDef(
    guid="9c7f3369-571f-5c4c-840b-22ff0c5169ae",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DaisysHelp.Name",
    display_name="Daisy's Help",
    searchable_by=["Daisy's Help", "Supporter"],
    subtypes=["Supporter"],
    collector_number=158,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=daisys_help,
)
