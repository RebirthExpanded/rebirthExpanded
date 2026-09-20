"""Multi Switch (SM - Guardians Rising 129/145 -- JP SM1+ 047/051, the art here).

Item.

  "Move an Energy from 1 of your Benched Pokemon to your Active Pokemon."

Energy Switch narrowed to Bench -> Active; any Energy card, not only
basic. Playable only with an Energy somewhere on the Bench.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef


def _bench_has_energy(board, player_id) -> bool:
    if board.active_pokemon(player_id) is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(board.attached_energies(p) for p in (bench.children if bench else []))


async def multi_switch(ctx):
    active = ctx.my_active()
    if active is None:
        return
    await ctx.move_energy_freely(ctx.my_bench(), [active], max_count=1,
                                 prompt="Choose an Energy to move to your Active Pokémon")


card = ItemCardDef(
    guid="57269e82-6082-5cd2-a23f-6bc21f101ac8",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item", "MultiSwitch"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=_bench_has_energy,
    effect=multi_switch,
)
