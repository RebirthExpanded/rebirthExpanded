"""Poké Vital A (SV065 62 -- JP SV6a 055; English SFA/62). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _any_damaged(board, player_id, card=None) -> bool:
    return any(_counters(board, p) > 0 for p in board.pokemon_in_play(player_id))


async def poke_vital_a(ctx):
    pool = [p for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your Pokémon to heal 150 damage from")
        if target is not None:
            await ctx.heal(150, target)


card = ItemCardDef(
    guid="8cfbfe19-cfee-56a6-8975-fef12c74591e",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeVitalA.Name",
    display_name="Poké Vital A",
    searchable_by=["Poké Vital A", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=62,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    condition=_any_damaged,
    effect=poke_vital_a,
)
card.stays_in_discard = True
