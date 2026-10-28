"""Fighting Au Lait (SV2 181 -- JP SV2P 067; English PAL/181). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _au_lait_condition(board, player_id, card=None) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    mine = board.find_player_area(player_id, "prizePile")
    theirs = board.find_player_area(other, "prizePile") if other else None
    return (mine is not None and theirs is not None and len(mine.children) > len(theirs.children)
            and any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id)))


async def fighting_au_lait(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 60 damage from")
        if target is not None:
            await ctx.heal(60, target)


card = ItemCardDef(
    guid="0643b530-7c52-5c6b-a376-37f03fdaec82",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingAuLait.Name",
    display_name="Fighting Au Lait",
    searchable_by=["Fighting Au Lait", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_au_lait_condition,
    effect=fighting_au_lait,
)
