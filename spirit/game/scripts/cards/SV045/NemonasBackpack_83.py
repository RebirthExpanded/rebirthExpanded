"""Nemona's Backpack (SV045 83 -- JP SV4a 160; English PAF/83). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _nemona(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Nemona"


def _nemona_in_discard(board, player_id, card=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_nemona(c) for c in discard.children)


async def nemonas_backpack(ctx):
    pool = [c for c in ctx.discard_pile() if _nemona(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Nemona cards")
        if picks:
            await ctx.put_in_hand(picks)


card = ItemCardDef(
    guid="c2297373-bd98-5132-8f59-9582389292e6",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NemonasBackpack.Name",
    display_name="Nemona's Backpack",
    searchable_by=["Nemona's Backpack", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_nemona_in_discard,
    effect=nemonas_backpack,
)
