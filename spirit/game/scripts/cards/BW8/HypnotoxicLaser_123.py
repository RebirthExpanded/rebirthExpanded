"""Hypnotoxic Laser (BW - Plasma Storm 123/135 -- JP BW7 063/070, the art
here).

Item.

  "Your opponent's Active Pokemon is now Poisoned. Flip a coin. If heads,
   your opponent's Active Pokemon is also Asleep."

Poison first, unconditionally; the coin decides Sleep on top. Both go
through apply_special_condition, so a Pokemon that cannot be affected (a
fossil) simply is not -- and Bent Spoon does not stop this, since it is an
Item, not an attack. Virbank City Gym's extra poison damage rides the
Poison the usual way.
"""

from spirit.game.attributes import Rarities, SpecialConditions
from spirit.game.data_utils import ItemCardDef


async def hypnotoxic_laser(ctx):
    """Poison their Active; heads adds Sleep."""
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.apply_special_condition(target, SpecialConditions.POISONED)
    heads = await ctx.flip_coins(1, title="Hypnotoxic Laser")
    if heads and heads[0]:
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


def _laser_playable(board, player_id) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    return opponent is not None and board.active_pokemon(opponent) is not None


card = ItemCardDef(
    guid="5a79cdc5-c088-52aa-852a-29da944fb5bb",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HypnotoxicLaser.Name",
    display_name="Hypnotoxic Laser",
    searchable_by=["Hypnotoxic Laser", "Item", "HypnotoxicLaser"],
    subtypes=["Item"],
    collector_number=123,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    condition=_laser_playable,
    effect=hypnotoxic_laser,
)
