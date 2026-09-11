"""Counter Catcher (SM - Crimson Invasion 91/111 -- JP SM8b 114/150, the art
here).

Item.  "You can play this card only if you have more Prize cards remaining
than your opponent. Switch 1 of your opponent's Benched Pokemon with their
Active Pokemon."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import more_prizes_remaining_than_opponent
from spirit.game.card_effects.trainers import player_has_bench
from spirit.game.data_utils import ItemCardDef


def _condition(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    return more_prizes_remaining_than_opponent(board, player_id) \
        and opponent is not None and player_has_bench(board, opponent)


async def counter_catcher(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch in")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="1d0c89f4-d830-59a5-91d6-c5f6a3ad75bb",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item", "CounterCatcher"],
    subtypes=["Item"],
    collector_number=91,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=counter_catcher,
)
