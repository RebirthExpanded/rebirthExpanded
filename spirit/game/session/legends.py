"""LEGEND (HGSS) assembly and departure.

Two physical halves in hand are played together as one Pokemon: a
runtime-only LegendPokemonEntity is created on the board with the halves
riding under it, and the client is told to build the combined card
(CreateLegend) from the two halves parked in the staging pile. When the
combined Pokemon leaves play -- Knocked Out, bounced, shuffled away -- the
halves go where the card would have gone, the attachments where they would
have gone, and the combined entity is destroyed on both peers.

Ported from Spirit-PTCGO (9f5d7eef) onto this engine's helpers.
"""

from typing import Any, Dict, List, Optional

from spirit.game.attributes import GameSequence
from spirit.game.data_utils import (
    LegendHalf, Triggers, def_for, matching_legend_halves, vunion_pieces_in,
)
from spirit.game.models.board import (
    CompositePartEntity, CompositePokemonEntity, LegendHalfEntity, LegendPokemonEntity,
    VUnionPieceEntity, VUnionPokemonEntity,
)
from spirit.game.models.card import Card
from spirit.game.session.passives import (
    effective_bench_capacity, putting_into_play_blocked,
)
from spirit.network.message_names import OutboundMsg


def pair_is_playable(session, player_id, first, second) -> bool:
    """Both halves in the acting player's hand, opposite halves of one
    LEGEND, a Bench slot free, no play lock on either, and a Bench the
    combined Pokemon may be put onto (Eternal Zone reads its live types)."""
    board = session.board_state
    hand = board.find_player_area(player_id, "hand")
    bench = board.find_player_area(player_id, "bench")
    if not isinstance(first, LegendHalfEntity) or not isinstance(second, LegendHalfEntity):
        return False
    # Reject stale copies that are no longer registered on this board.
    if board.get_entity(first.entity_id) is not first \
            or board.get_entity(second.entity_id) is not second:
        return False
    if hand is None or first.parent is not hand or second.parent is not hand:
        return False
    if first.owning_player_id != player_id or second.owning_player_id != player_id:
        return False
    if bench is None or len(bench.children) >= effective_bench_capacity(board, player_id):
        return False
    if not matching_legend_halves(first, second):
        return False
    state = session.turn_state
    if state.play_locked(player_id, first) or state.play_locked(player_id, second):
        return False
    # "Can't put into play" locks read the card going down: a half carries
    # the combined Pokemon's types.
    if putting_into_play_blocked(board, player_id, first):
        return False
    return True


async def execute_play(session, player_id, card, entry, target_ids) -> bool:
    """The hand play: pick the partner half when several match, assemble,
    then the combined Pokemon's on-play abilities."""
    bench = session.board_state.find_player_area(player_id, "bench")
    if bench is None or session._validated_target(entry, target_ids) != bench.entity_id:
        return False
    hand = session.board_state.find_player_area(player_id, "hand")
    partners = [other for other in (hand.children if hand else [])
                if pair_is_playable(session, player_id, card, other)]
    if not partners:
        return False
    if len(partners) > 1:
        picked = await session.prompt_card_chooser(
            player_id, card.entity_id, partners, 1,
            prompt="Choose the other half of this LEGEND",
        )
        partners = [other for other in partners if other.entity_id in picked]
        if len(partners) != 1:
            return False
    legend = await assemble_legend(session, player_id, card, partners[0])
    if legend is None:
        return False
    return bool(await session._fire_triggered_abilities(player_id, legend, Triggers.ON_PLAY))


def build_legend_model(definition) -> Card:
    """The server Card model of a combined definition (never published)."""
    archetype = definition.to_archetype_dict()
    return Card(definition.guid, definition.key, archetype["attributes"],
                definition.display_name, definition.searchable_by, definition.subtypes)


async def assemble_legend(session, player_id, first, second) -> Optional[LegendPokemonEntity]:
    """Play two compatible halves from hand as one Benched Pokemon."""
    if not pair_is_playable(session, player_id, first, second):
        return None
    first_def = def_for(first.archetype_id)
    definition = first_def.legend_definition
    top, bottom = ((first, second) if first_def.half == LegendHalf.TOP else (second, first))
    legend = LegendPokemonEntity(build_legend_model(definition), top, bottom, player_id)
    board = session.board_state
    bench = board.find_player_area(player_id, "bench")
    staging = board.find_global_area("outOfPlay")
    position = board.free_bench_slot(player_id)
    staging.add_child(legend)
    board._register_entity(legend)
    added = session._build_msg(OutboundMsg.ENTITY_ADDED.value, {
        "gameID": session.game_id, "entityID": legend.entity_id,
        "owningPlayerID": player_id, "parentEntityID": staging.entity_id,
    })
    for half in (top, bottom):
        board.attach_card(half.entity_id, legend.entity_id)
    board.move_card(legend.entity_id, bench.entity_id)
    legend.owning_player_id = player_id
    session.turn_state.mark_entered_play(legend.entity_id)
    viewers = list(session.players.values())
    # ConfigureLegendary immediately dereferences both already-introduced halves.
    await session.send_game_sequence(
        viewers, GameSequence.SERIAL_SEQUENCE,
        [session._entity_introduced_msg(top), session._entity_introduced_msg(bottom)])
    await session.send_game_sequence(
        viewers, GameSequence.SERIAL_SEQUENCE,
        [added, session._entity_introduced_msg(legend)])
    # The renderer follows the half ids; ordinary child links would list the
    # halves in the zoom stack and break the two-position LEGEND render, so
    # the client parks them in the staging pile.
    client_staging = board.client_out_of_play_children()
    await session.send_game_sequence(viewers, GameSequence.CREATE_LEGEND, [
        session._entity_moved_msg(top.entity_id, staging.entity_id,
                                  client_staging.index(top), stamp_slot=False),
        session._entity_moved_msg(bottom.entity_id, staging.entity_id,
                                  client_staging.index(bottom), stamp_slot=False),
        session._entity_moved_msg(legend.entity_id, bench.entity_id, position),
    ])
    await session.fire_pokemon_benched_triggers(player_id, legend)
    return legend


def legend_members(legend: LegendPokemonEntity) -> List[Any]:
    """Every card under the combined Pokemon, halves included, depth-first."""
    members = []
    pending = list(legend.children)
    while pending:
        member = pending.pop(0)
        members.append(member)
        pending.extend(member.children)
    return members


def depart_legend(session, legend, destination, *, move_with=None, position=None,
                  destinations: Optional[Dict[str, Any]] = None):
    """The combined Pokemon (a LEGEND or a V-UNION) leaves play: its parts go to `destination`,
    every other member to the owner's discard -- or, when `destinations`
    maps an entity id to an area (the Knock Out path's per-card routing:
    Lost City, U-Turn Board, a Prism Star), there. `move_with` names
    attachments that travel with the halves. Returns (messages, members);
    the combined entity is unregistered and destroyed on both peers."""
    board = session.board_state
    if board.get_entity(legend.entity_id) is not legend:
        return [], []
    move_with = set(move_with or ())
    destinations = destinations or {}
    owner = legend.owning_player_id
    discard = board.find_player_area(owner, "discard")
    staging = board.find_global_area("outOfPlay")
    members = legend_members(legend)
    messages = []
    viz = session._clear_entity_visualizations_msg(legend)
    if viz is not None:
        messages.append(viz)
    session.clear_pokemon_effects(legend)
    session.reset_pokemon_damage(legend)
    session.reset_ability_usage(legend)
    # The client's Knockout executor needs a move whose source is the
    # combined Pokemon.
    messages.append(session._entity_moved_msg(
        legend.entity_id, staging.entity_id, len(board.client_out_of_play_children())))
    board.move_card(legend.entity_id, staging.entity_id)
    legend.owning_player_id = owner
    halves = tuple(legend.parts)
    for member in members:
        if member in halves or member.entity_id in move_with:
            area = destination
        else:
            area = destinations.get(member.entity_id, discard)
        slot = position if area is destination and position is not None else len(area.children)
        if member in halves:
            legend.remove_child(member)
        board.move_card(member.entity_id, area.entity_id, position=slot)
        viz = session._clear_entity_visualizations_msg(member)
        if viz is not None:
            messages.append(viz)
        messages.append(session._entity_moved_msg(member.entity_id, area.entity_id, slot))
    staging.remove_child(legend)
    board._unregister_entity(legend)
    session.turn_state.entered_play_turn.pop(legend.entity_id, None)
    messages.append(session._build_msg(OutboundMsg.ENTITY_DESTROYED.value, {
        "gameID": session.game_id, "entityID": legend.entity_id,
    }))
    return messages, members


# --- Pokemon V-UNION ----------------------------------------------------------

def vunion_used(board, player_id: str, definition) -> bool:
    """Whether `player_id` has already combined this V-UNION this game
    (kept on the board, where the offer's condition can read it)."""
    used = getattr(board, "vunion_assembled", None) or {}
    return definition.guid.lower() in used.get(player_id, set())


def vunion_assembly_pieces(board, player_id: str, piece) -> Optional[List[Any]]:
    """The four pieces of `piece`'s V-UNION sitting in `player_id`'s discard
    pile (corner order), when the assembly is possible right now: once per
    game for that V-UNION, a Bench slot free, and a Bench the combined
    Pokemon may be put onto. None otherwise."""
    definition = getattr(def_for(piece.archetype_id), "vunion_definition", None)
    if definition is None:
        return None
    if vunion_used(board, player_id, definition):
        return None
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    if discard is None or bench is None:
        return None
    if piece.parent is not discard or piece.owning_player_id != player_id:
        return None
    if len(bench.children) >= effective_bench_capacity(board, player_id):
        return None
    if putting_into_play_blocked(board, player_id, piece):
        return None
    return vunion_pieces_in(discard.children, definition)


async def assemble_vunion(session, player_id: str, piece) -> Optional[VUnionPokemonEntity]:
    """Combine the four pieces from the discard pile onto the Bench as one
    Pokemon V-UNION. Once per game per V-UNION; not an Ability, so no
    Ability lock reaches it."""
    board = session.board_state
    pieces = vunion_assembly_pieces(board, player_id, piece)
    if pieces is None:
        return None
    definition = def_for(piece.archetype_id).vunion_definition
    union = VUnionPokemonEntity(build_legend_model(definition), pieces, player_id)
    bench = board.find_player_area(player_id, "bench")
    staging = board.find_global_area("outOfPlay")
    position = board.free_bench_slot(player_id)
    staging.add_child(union)
    board._register_entity(union)
    added = session._build_msg(OutboundMsg.ENTITY_ADDED.value, {
        "gameID": session.game_id, "entityID": union.entity_id,
        "owningPlayerID": player_id, "parentEntityID": staging.entity_id,
    })
    for part in pieces:
        board.attach_card(part.entity_id, union.entity_id)
    board.move_card(union.entity_id, bench.entity_id)
    union.owning_player_id = player_id
    session.turn_state.mark_entered_play(union.entity_id)
    used = getattr(board, "vunion_assembled", None)
    if used is None:
        used = board.vunion_assembled = {}
    used.setdefault(player_id, set()).add(definition.guid.lower())
    viewers = list(session.players.values())
    # The pieces are public already (discard pile); the combined Pokemon is
    # a new entity both viewers learn, then the four fly into the join slots
    # and the combined card lands on the Bench (the client's CreateVUnion
    # executor reads the moves of this bracket).
    await session.send_game_sequence(
        viewers, GameSequence.SERIAL_SEQUENCE,
        [added, session._entity_introduced_msg(union)])
    client_staging = board.client_out_of_play_children()
    moves = [
        session._entity_moved_msg(part.entity_id, staging.entity_id,
                                  client_staging.index(part), stamp_slot=False)
        for part in pieces
    ]
    moves.append(session._entity_moved_msg(union.entity_id, bench.entity_id, position))
    await session.send_game_sequence(viewers, GameSequence.CREATE_VUNION, moves)
    await session.fire_pokemon_benched_triggers(player_id, union)
    return union
