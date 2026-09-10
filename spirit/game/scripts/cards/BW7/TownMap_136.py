"""Town Map (BW - Boundaries Crossed 136/149).

Item.

  "Turn all of your Prize cards face up. (Those Prize cards remain face up
   for the rest of the game.)"

Nothing else in the pool turns a card face up where it lies. The nearest
thing, the "look at your Prize cards" reveal behind Prize-searching cards,
is the opposite: it introduces the Prizes to the picker alone and the
caller re-hides them with AttributesReset the moment the fan closes.

So this does not send a reveal at all -- it sets CardEntity.face_up, the
override in is_hidden_from, which is the single gate every serialization
runs through. That is what makes the flip permanent AND survive a
reconnect: the SGS is the sole source of truth for a fresh client, and it
reads the same check, so the Prizes come back face up rather than as card
backs. A one-off EntityIntroduced would look right until someone
reconnected.

Face up means face up on the table, so the intro goes to BOTH players --
the opponent gets to see them too. The owner's own Prizes are the only
ones affected; the opponent's stay hidden.

Prizes are dealt once at setup and only ever leave, so flipping what is
in the pile now covers the rest of the game. A Prize taken into hand is
already visible to its owner, and face_up rides along with the card
without changing that.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _has_prizes(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "prizePile")
    return bool(area and area.children)


async def town_map(ctx):
    """Turn the player's own Prize cards face up, for good."""
    area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(area.children) if area else []
    if not prizes:
        return
    for prize in prizes:
        prize.face_up = True
    # Both viewers, since the cards are now face up on the table.
    for viewer_id in (ctx.player_id, ctx.opponent_id):
        for prize in prizes:
            ctx._queue(ctx.session._entity_introduced_msg(prize),
                       viewer_id=viewer_id)


card = ItemCardDef(
    guid="05396c65-9f46-518e-a9db-9173574366f0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map", "Item", "TownMap"],
    subtypes=["Item"],
    collector_number=136,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=town_map,
    condition=_has_prizes,
)
