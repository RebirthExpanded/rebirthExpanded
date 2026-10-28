"""Grusha (SV2 184 -- JP SV2P 068; English PAL/184, PAL/253, PAL/268). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.models.board import EnergyEntity


async def grusha(ctx):
    bare = not any(isinstance(c, EnergyEntity) for p in ctx.my_pokemon_in_play() for c in p.children)
    await ctx.draw_until(7 if bare else 5)


card = SupporterCardDef(
    guid="6d23b4fd-9e42-50f3-b03b-c7641ac34aab",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grusha.Name",
    display_name="Grusha",
    searchable_by=["Grusha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=grusha,
)
