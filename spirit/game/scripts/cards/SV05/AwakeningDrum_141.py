"""Awakening Drum (SV05 141 -- JP SV5K 062; English TEF/141). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])


async def awakening_drum(ctx):
    n = sum(1 for p in ctx.my_pokemon_in_play() if _has_sub(p, "Ancient"))
    if n:
        await ctx.draw_cards(n)


card = ItemCardDef(
    guid="41c761ef-6bf0-528d-bace-fde33b5e2f2e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AwakeningDrum.Name",
    display_name="Awakening Drum",
    searchable_by=["Awakening Drum", "Item", "Ancient", "ACE SPEC"],
    subtypes=["Item", "Ancient", "ACE SPEC"],
    collector_number=141,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=awakening_drum,
)
