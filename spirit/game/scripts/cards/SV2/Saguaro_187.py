"""Saguaro (SV2 187 -- JP SV2D 068; English PAL/187, PAL/255, PAL/270). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _any_damaged(board, player_id, card=None) -> bool:
    return any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def saguaro(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=1, prompt="Choose up to 2 of your Pokémon to heal 50 damage from")
    for p in picks:
        await ctx.heal(50, p)


card = SupporterCardDef(
    guid="688d92fa-2e49-57eb-a75b-fc4a81d5d723",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Saguaro.Name",
    display_name="Saguaro",
    searchable_by=["Saguaro", "Supporter"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_any_damaged,
    effect=saguaro,
)
