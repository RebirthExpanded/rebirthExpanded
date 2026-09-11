"""Great Catcher (SM - Cosmic Eclipse 192/236 -- JP SM11a 052/064).

Item.

  "You can play this card only if you discard 2 other cards from your
   hand. Switch 1 of your opponent's Benched Pokemon-GX or Pokemon-EX with
   their Active Pokemon."

A gust: the switch is done to the Benched GX/EX it drags up.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import ItemCardDef, subtypes_for


def _gx_or_ex(pokemon) -> bool:
    return any(s in ("GX", "EX") for s in subtypes_for(pokemon.archetype_id))


def _condition(board, player_id, pokemon=None) -> bool:
    if not requires_hand(None, 2)(board, player_id):
        return False
    bench = board.find_player_area(board.player_ids[1] if board.player_ids[0] == player_id else board.player_ids[0], "bench")
    return any(_gx_or_ex(p) for p in (bench.children if bench else []))


async def great_catcher(ctx):
    paid = await ctx.discard_from_hand(2, prompt="Discard 2 cards for Great Catcher")
    if len(paid) < 2:
        return
    targets = [p for p in ctx.opponent_bench() if _gx_or_ex(p)]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon-GX or Pokémon-EX to switch in")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = ItemCardDef(
    guid="0638ec8b-fbec-5de4-85b5-4f39a4d80b81",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatCatcher.Name",
    display_name="Great Catcher",
    searchable_by=["Great Catcher", "Item", "GreatCatcher"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    condition=_condition,
    effect=great_catcher,
)
