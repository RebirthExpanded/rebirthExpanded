"""Repel (SM - Sun & Moon 130/149 -- JP SM1S 055/060).

Item.

  "Your opponent switches their Active Pokemon with 1 of their Benched
   Pokemon."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.data_utils import ItemCardDef


def _opponent_has_bench(board, player_id, pokemon=None) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    bench = board.find_player_area(opponent, "bench") if opponent else None
    return bool(bench and bench.children)


async def repel(ctx):
    active = ctx.opponent_active()
    if active is not None and not ctx.effects_blocked(active):
        await opponent_switches(ctx)


card = ItemCardDef(
    guid="54a848e2-6e46-594a-84ee-258cef7b234b",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item", "Repel"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    condition=_opponent_has_bench,
    effect=repel,
)
