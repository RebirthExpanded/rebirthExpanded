"""Ogre's Mask (SV085 118 -- JP SV6 090; English PRE/118, TWM/159). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.data_utils import def_for, subtypes_for


def _ogerpon_ex(card) -> bool:
    d = def_for(card.archetype_id)
    return card is not None and "Ogerpon" in (getattr(d, "display_name", "") or "") and "ex" in (subtypes_for(card.archetype_id) or [])


def _ogres_mask_condition(board, player_id, card=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return (bool(discard) and any(_ogerpon_ex(c) for c in discard.children)
            and any(_ogerpon_ex(p) for p in board.pokemon_in_play(player_id)))


async def ogres_mask(ctx):
    pool = [c for c in ctx.discard_pile() if _ogerpon_ex(c)]
    mine = [p for p in ctx.my_pokemon_in_play() if _ogerpon_ex(p)]
    if not pool or not mine:
        return
    incoming = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Ogerpon ex in your discard pile")
    outgoing = await ctx.choose_pokemon(mine, "Choose an Ogerpon ex in play to switch with it") if incoming else None
    if outgoing is not None:
        await ctx.session.perform_identity_swap(outgoing, incoming[0], "discard", True, ctx=ctx)


card = ItemCardDef(
    guid="aeb43d46-a6fd-5bf1-8757-84d8c02e9003",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OgresMask.Name",
    display_name="Ogre's Mask",
    searchable_by=["Ogre's Mask", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_ogres_mask_condition,
    effect=ogres_mask,
)
