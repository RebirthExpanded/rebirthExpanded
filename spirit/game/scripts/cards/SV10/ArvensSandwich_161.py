"""Arven's Sandwich (SV10 161 -- JP SV9a 057; English DRI/161). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _active_damaged(board, player_id, card=None) -> bool:
    active = board.active_pokemon(player_id)
    return active is not None and active.get_attribute(AttrID.HP, 0) < effective_max_hp(board, active)


async def arvens_sandwich(ctx):
    active = ctx.board.active_pokemon(ctx.player_id)
    if active is None:
        return
    name = getattr(def_for(active.archetype_id), "display_name", "") or ""
    await ctx.heal(100 if name.startswith("Arven's ") else 30, active)


card = ItemCardDef(
    guid="7e1efcbf-7dde-543d-88c5-2403e34bf1b0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArvensSandwich.Name",
    display_name="Arven's Sandwich",
    searchable_by=["Arven's Sandwich", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=_active_damaged,
    effect=arvens_sandwich,
)
