"""Ash's Friendship (SMD 25 -- JP SMD 025; English Japan only). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.data_utils import def_for, subtypes_for


async def _ashs_friendship(ctx):
    """Draw 2 cards. If you have Ash's Pikachu-GX in play, draw 2 more cards."""
    await ctx.draw_cards(2)
    if any(getattr(def_for(p.archetype_id), "display_name", "") == "Ash's Pikachu-GX"
           for p in ctx.my_pokemon_in_play()):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="0215ac62-984c-52b5-b942-bf92b2b05a91",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AshsFriendship.Name",
    display_name="Ash's Friendship",
    searchable_by=["Ash's Friendship", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.Common,
    effect=_ashs_friendship,
)
