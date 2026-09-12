"""Behaviors for the Trainer cards of the Lugia VSTAR and Mew VMAX decks."""

import re

from spirit.game.attributes import (
    AttrID, CardType, CLIENT_POKEMON_TYPE_NAMES, PokemonStage, PokemonTypes, TrainerType,
)
from spirit.game.models.board import PokemonEntity
from spirit.game.data_utils import (
    Ability, Activations, Attack, def_for, has_rule_box, is_pokemon_v,
    subtypes_for, Triggers,
)
from spirit.game.session.constants import BENCH_CAPACITY, PROMPT_CHOOSE_A_PRIZE
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_basic_pokemon_in_play,
    is_evolution_pokemon,
    is_item_card,
    is_basic_energy,
    is_energy_card,
    is_energy_of_type,
    is_pokemon_card,
    is_pokemon_of_type,
    is_pokemon_tool,
    is_special_energy,
    is_supporter_card,
    is_water_pokemon,
)
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import (
    Passive,
    trainer_targeting_blocked,
    TurnDamageModifier,
    carrier_pokemon,
    effective_bench_capacity,
    effective_max_hp,
    trainer_play_blocked,
)


# --- Shared playability predicates -----------------------------------------

def hand_size_at_least(count: int):
    """Condition: the hand holds `count` cards INCLUDING the trainer itself."""
    def check(board, player_id):
        hand = board.find_player_area(player_id, "hand")
        return hand is not None and len(hand.children) >= count
    return check


def _bench_pokemon(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return [c for c in (bench.children if bench else [])
            if isinstance(c, PokemonEntity)]


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def opponent_has_bench(board, player_id):
    opponent = _other_player(board, player_id)
    return bool(opponent) and bool(_bench_pokemon(board, opponent))


def player_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id))


def someone_has_bench(board, player_id):
    return bool(_bench_pokemon(board, player_id)) or opponent_has_bench(board, player_id)


def has_supporter_in_discard(board, player_id):
    return any(is_supporter_card(c) for c in _discard(board, player_id))


def has_discard_card(board, player_id):
    return bool(_discard(board, player_id))


def opponent_prizes_low(board, player_id):
    """Roxanne's gate: the opponent has 3 or fewer Prize cards remaining."""
    opponent = _other_player(board, player_id)
    if not opponent:
        return False
    area = board.find_player_area(opponent, "prizePile")
    return bool(area) and len(area.children) <= 3


def battle_vip_pass_playable(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None or turn_state.turn_number > 2:
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and len(bench.children) < BENCH_CAPACITY


def has_other_item_in_hand(board, player_id):
    """Cram-o-matic's gate: another Item card besides itself sits in hand."""
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_item_card(c)) >= 2


def deck_nonempty(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck) and bool(deck.children)


def _opponent_special_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_special_energy(c))
    return out


def opponent_has_special_energy(board, player_id):
    return bool(_opponent_special_energies(board, player_id))


def _discard(board, player_id):
    area = board.find_player_area(player_id, "discard")
    return list(area.children) if area else []


# "Ball" as a whole word: Great Ball and Poke Ball yes, Air Balloon no.
_BALL_IN_NAME = re.compile(r"\bball\b")
# ...and not every English "Ball" is a Poke Ball. The rule the card states is
# the Japanese one -- a Goods card whose name carries ボール -- so a name that
# picks the word up only in translation is not a Ball card. Delicious Onigiri
# (ME6 63) is the live case: おいしいおむすび says nothing about ボール, but
# rendered as a "Rice Ball" it would read as one here. Any future rendering
# that does the same belongs in this pattern.
_NOT_A_POKE_BALL = re.compile(r"\brice ball\b")


def is_basic_energy_card(card) -> bool:
    return is_basic_energy(card)


def is_metal_energy_card(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.METAL)


def is_grass_energy_card(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.GRASS)


def is_darkness_pokemon(card) -> bool:
    return is_pokemon_of_type(card, PokemonTypes.DARKNESS)


def is_pokemon_vmax(archetype_id) -> bool:
    return "VMAX" in subtypes_for(archetype_id)


def has_basic_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(is_basic_energy_card(c) for c in hand.children)


def bede_playable(board, player_id) -> bool:
    return player_has_bench(board, player_id) and has_basic_energy_in_hand(board, player_id)


def _opponent_energies(board, player_id):
    opponent = _other_player(board, player_id)
    if not opponent:
        return []
    out = []
    for pokemon in board.pokemon_in_play(opponent):
        out.extend(c for c in pokemon.children if is_energy_card(c))
    return out


def opponent_has_energy_attached(board, player_id) -> bool:
    return bool(_opponent_energies(board, player_id))


def _my_vmax_pokemon(board, player_id):
    return [p for p in board.pokemon_in_play(player_id) if is_pokemon_vmax(p.archetype_id)]


def has_vmax_in_play(board, player_id) -> bool:
    return bool(_my_vmax_pokemon(board, player_id))


def has_two_metal_energy_in_hand(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and sum(1 for c in hand.children if is_metal_energy_card(c)) >= 2


def _tools_and_stadium(board):
    """Every attached Pokemon Tool plus the Stadium in play, both sides.

    Field Blower and Lost Vacuum are Items, so a Stadium that shields itself
    from Item and Supporter effects (Thunder Mountain) is not a target.
    """
    targets = []
    for pid in board.player_ids:
        for pokemon in board.pokemon_in_play(pid):
            targets.extend(c for c in pokemon.children if is_pokemon_tool(c))
    stadium_area = board.find_global_area("activeStadium")
    targets.extend(
        c for c in (stadium_area.children if stadium_area else [])
        if not trainer_targeting_blocked(board, c)
    )
    return targets


def tools_or_stadium_in_play(board, player_id=None):
    return bool(_tools_and_stadium(board))


def lost_vacuum_playable(board, player_id):
    return hand_size_at_least(2)(board, player_id)         and tools_or_stadium_in_play(board)


def serena_playable(board, player_id):
    if hand_size_at_least(2)(board, player_id):
        return True
    opponent = _other_player(board, player_id)
    return bool(opponent) and any(
        is_pokemon_v(p.archetype_id) for p in _bench_pokemon(board, opponent)
    )


# --- Supporters -------------------------------------------------------------

async def professors_research(ctx):
    """Discard your hand and draw 7 cards."""
    await ctx.discard_cards(ctx.hand())
    await ctx.draw_cards(7)


def marnie_playable(board, player_id, card=None):
    """Marnie needs at least one card between the two hands, this Marnie
    aside.

    "Each player shuffles their hand and puts it on the bottom of their
    deck. THEN, you draw 5 cards." A "Then," (or "If you do") clause does
    not happen when the step before it could not be carried out at all, so
    with both hands empty nothing goes under a deck and nobody draws --
    the card would do nothing, and a card that does nothing may not be
    played. One card in either hand is enough to set the whole thing off.
    """
    total = 0
    for pid in board.player_ids:
        hand = board.find_player_area(pid, "hand")
        for c in (hand.children if hand else []):
            if pid == player_id and card is not None and c is card:
                continue    # the copy being played is not in hand any more
            total += 1
    return total > 0


async def marnie(ctx):
    """Both players shuffle their hands under their decks; you draw 5, the
    opponent draws 4. Per player in sequence: shuffle-to-bottom, then draw."""
    await ctx.hand_to_bottom_of_deck(ctx.player_id)
    await ctx.draw_cards(5)
    await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    await ctx.draw_cards(4, ctx.opponent_id)


async def bosss_orders(ctx):
    """Switch 1 of the opponent's Benched Pokemon with their Active."""
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


async def serena(ctx):
    """Choose 1: discard up to 3 then draw to 5, OR gust a Benched Pokemon V."""
    v_bench = [p for p in ctx.opponent_bench() if is_pokemon_v(p.archetype_id)]
    can_discard = bool(ctx.hand())
    if can_discard and v_bench:
        gust = await ctx.choose(
            "Choose 1:", ["Discard up to 3 cards from your hand. If you do, draw cards until you have 5 cards in your hand.", 
                          "Switch 1 of your opponent's Benched Pokemon V with their Active Pokemon."]
        ) == 1
    else:
        gust = bool(v_bench)
    if gust:
        target = await ctx.choose_pokemon(
            v_bench, "Choose the opponent's new Active Pokémon"
        )
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return
    discarded = await ctx.discard_from_hand(
        3, minimum=1, prompt="Choose up to 3 cards to discard"
    )
    if discarded:
        await ctx.draw_until(5)


async def irida(ctx):
    """Search the deck for up to 1 Water Pokemon and up to 1 Item card."""
    water, items = await ctx.search_deck_groups(
        [
            # loc keys render the {W} energy icon in the slot labels
            (is_water_pokemon, 1, "playmat.prompt.selectapokemonwater"),
            (is_item_card, 1, "playmat.prompt.select1item"),
        ],
        prompt="Choose up to 1 Water Pokémon and up to 1 Item card",
    )
    await ctx.put_in_hand(water + items, reveal=True)
    await ctx.shuffle_deck()


async def arven(ctx):
    """Search the deck for up to 1 Item card and up to 1 Pokemon Tool card."""
    items, tools = await ctx.search_deck_groups(
        [
            (is_item_card, 1, "playmat.prompt.select1item"),
            (is_pokemon_tool, 1, "playmat.prompt.selectapoketoolcard"),
        ],
        prompt="Choose up to 1 Item card and up to 1 Pokémon Tool card",
    )
    await ctx.put_in_hand(items + tools, reveal=True)
    await ctx.shuffle_deck()


async def pal_pad(ctx):
    """Shuffle up to 2 Supporter cards from your discard pile into your deck."""
    picks = await ctx.choose_cards(
        [c for c in ctx.discard_pile() if is_supporter_card(c)], 2, minimum=1,
        prompt="Choose up to 2 Supporter cards to shuffle into your deck",
    )
    await ctx.shuffle_into_deck(picks)


async def judge(ctx):
    """Each player shuffles their hand into their deck and draws 4 cards."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(4, pid)


async def roxanne(ctx):
    """Opponent has 3 or fewer Prize cards remaining: each player shuffles
    their hand into their deck, then you draw 6 and the opponent draws 2."""
    for pid, count in ((ctx.player_id, 6), (ctx.opponent_id, 2)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(count, pid)


async def cyllene(ctx):
    """Flip 2 coins; put up to that many cards from your discard pile on
    top of your deck, in an order you choose."""
    heads = await ctx.flip_coins(2, "Cyllene")
    count = heads.count(True)
    if count <= 0:
        return
    picks = await ctx.choose_cards(
        ctx.discard_pile(), count, minimum=1, ordered=True,
        prompt="Choose cards to put on top of your deck, in order",
    )
    # Ordered picks stack in selection order -- the last one picked ends up
    # on top of the deck.
    for card in picks:
        await ctx.put_on_top_of_deck(card)


async def piers(ctx):
    """Search your deck for an Energy card and a Darkness Pokemon, reveal
    them, and put them into your hand. Then, shuffle your deck."""
    energy, darkness = await ctx.search_deck_groups(
        [
            (is_energy_card, 1, "Energy card"),
            (is_darkness_pokemon, 1, "Darkness Pokémon"),
        ],
        prompt="Choose an Energy card and a Darkness Pokémon",
    )
    await ctx.put_in_hand(energy + darkness, reveal=True)
    await ctx.shuffle_deck()


async def bede(ctx):
    """Attach a basic Energy card from your hand to 1 of your Benched Pokemon."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    picked = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach it to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


async def team_yell_grunt(ctx):
    """Put an Energy attached to 1 of the opponent's Pokemon into their hand."""
    targets = _opponent_energies(ctx.board, ctx.player_id)
    picked = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy card to return to its owner's hand",
    )
    # Already visible in play (attached), so no reveal-on-move is needed.
    await ctx.put_in_hand(picked, reveal=False)


async def milo(ctx):
    """Discard up to 2 cards from your hand, and draw 2 cards for each card
    you discarded in this way."""
    discarded = await ctx.discard_from_hand(
        2, minimum=0, prompt="Choose up to 2 cards to discard"
    )
    if discarded:
        await ctx.draw_cards(2 * len(discarded))


async def sonia(ctx):
    """Search your deck for up to 2 Basic Pokemon or up to 2 basic Energy
    cards, reveal them, and put them into your hand. Then, shuffle your deck."""
    want_energy = await ctx.choose(
        "Choose 1:", ["Up to 2 Basic Pokémon", "Up to 2 basic Energy cards"]
    ) == 1
    predicate = is_basic_energy_card if want_energy else is_basic_pokemon
    picks = await ctx.search_deck(
        predicate, count=2, minimum=0,
        prompt="Choose up to 2 Basic Pokémon or up to 2 basic Energy cards.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def kabu(ctx):
    """Shuffle your hand into your deck. Then, draw 4 cards; draw 8 instead
    if your Active Pokemon is your only Pokemon in play."""
    await ctx.shuffle_into_deck(ctx.hand())
    only_active = len(ctx.my_pokemon_in_play()) <= 1
    await ctx.draw_cards(8 if only_active else 4)


async def rose(ctx):
    """Attach up to 2 basic Energy cards from your discard pile to 1 of your
    Pokemon VMAX. If you attached any this way, discard your hand."""
    target = await ctx.choose_pokemon(
        _my_vmax_pokemon(ctx.board, ctx.player_id), "Choose your Pokémon VMAX"
    )
    if target is None:
        return
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 basic Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)
    if picks:
        await ctx.discard_cards(ctx.hand())


async def hop(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


async def adaman(ctx):
    """Discard 2 Metal Energy cards from your hand, then search your deck
    for up to 2 cards and put them into your hand. Then, shuffle your deck."""
    discarded = await ctx.discard_from_hand(
        2, predicate=is_metal_energy_card,
        prompt="Discard 2 Metal Energy cards for Adaman",
    )
    if len(discarded) < 2:
        return
    picks = await ctx.search_deck(
        None, count=2, minimum=0, prompt="Choose up to 2 cards to put into your hand.",
    )
    # No "reveal it" clause on this card's text.
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def gardenias_vigor(ctx):
    """Draw 2 cards. If you drew any this way, attach up to 2 Grass Energy
    cards from your hand to 1 of your Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if not drawn:
        return
    energies = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not energies:
        return
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose the Benched Pokémon to attach Grass Energy to",
        optional=True,
    )
    if target is None:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0, prompt="Choose up to 2 Grass Energy cards to attach",
    )
    for energy in picks:
        await ctx.attach_energy(energy, target)


async def kamado(ctx):
    """Choose a card in your hand, and discard the other cards. If you do,
    draw 4 cards."""
    hand = ctx.hand()
    if not hand:
        return
    keep = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card to keep in your hand"
    )
    if not keep:
        return
    await ctx.discard_cards([c for c in hand if c is not keep[0]])
    await ctx.draw_cards(4)


async def zisu(ctx):
    """Draw cards until you have 1 more card in your hand than your opponent."""
    await ctx.draw_until(ctx.hand_size(ctx.opponent_id) + 1)


def _center_lady_targets(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if p.get_attribute(AttrID.SPECIAL_CONDITIONS)
        or p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
    ]


def center_lady_playable(board, player_id) -> bool:
    return bool(_center_lady_targets(board, player_id))


async def pokemon_center_lady(ctx):
    """Heal 60 damage from 1 of your Pokemon, and it recovers from all
    Special Conditions."""
    target = await ctx.choose_pokemon(
        _center_lady_targets(ctx.board, ctx.player_id), "Choose a Pokémon to heal"
    )
    if target is None:
        return
    await ctx.heal(60, target)
    await ctx.cure_all_conditions(target)


# --- Items -------------------------------------------------------------------

async def switch(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon."""
    target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def catcher_switch_both(ctx):
    """Drag up one of the opponent's Benched Pokemon, then switch your own.

    Guzma's text as a Supporter, Prime Catcher's as an ACE SPEC Item -- the
    same two switches, in the same order, with the second gated on the first
    ("if you do"). Gate playability with opponent_has_bench: with nothing to
    drag up the card does nothing at all.
    """
    target = await ctx.choose_pokemon(
        ctx.opponent_bench(), "Choose the opponent's new Active Pokémon"
    )
    if target is None:
        return
    # "If you do": a gust that a shield turns away (Omega Barrier) ends the
    # card here, and the player's own switch never happens.
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    my_bench = ctx.my_bench()
    if not my_bench:
        return
    mine = await ctx.choose_pokemon(
        my_bench, "Choose your new Active Pokémon"
    )
    if mine is not None:
        await ctx.switch_active(ctx.player_id, mine)


async def quick_ball(ctx):
    """Discard 1 other card, then search the deck for a Basic Pokemon."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card for Quick Ball"):
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def ultra_ball(ctx):
    """Discard 2 other cards, then search the deck for any Pokemon."""
    if len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Ultra Ball")) < 2:
        return
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def is_ball_item(card) -> bool:
    """An Item card with "Ball" in its name (Ball Guy).

    "Ball" is a WORD in the name, not a run of letters: Air Balloon is not a
    Ball card -- and is a Pokemon Tool rather than an Item besides, which is
    the other half of why it is out of reach. Nor is every "Ball" a Poke Ball:
    a name that only gains the word in English (a "Rice Ball") is not one
    either, which _NOT_A_POKE_BALL is for.
    """
    if not is_item_card(card):
        return False
    definition = def_for(getattr(card, "archetype_id", None) or "")
    name = (getattr(definition, "display_name", None) or "").lower()
    return bool(_BALL_IN_NAME.search(name) and not _NOT_A_POKE_BALL.search(name))


async def ball_guy(ctx):
    """Up to 3 DIFFERENT Item cards with "Ball" in their name, out of the
    deck and into your hand.

    "3 different" is by name, so a deck holding four Quick Balls offers one
    of them; the chooser sees the whole deck behind the candidates so the
    player can count what is left.
    """
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_names = set()
    for card_entity in deck_cards:
        if not is_ball_item(card_entity):
            continue
        definition = def_for(card_entity.archetype_id)
        name = definition.display_name if definition else None
        if not name or name in seen_names:
            continue
        seen_names.add(name)
        reps.append(card_entity)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 different Item cards with \"Ball\" in their name.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def evolution_incense(ctx):
    """Search the deck for an Evolution Pokemon."""
    picks = await ctx.search_deck(
        is_evolution_pokemon, count=1, minimum=0,
        prompt="Choose an Evolution Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def escape_rope(ctx):
    """Each player switches their Active with a Benched Pokemon; the opponent
    chooses first and their swap is shown to both clients before the Escape
    Rope player decides (no Bench, no switch)."""
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        target = await ctx.choose_pokemon(
            opp_bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
        )
        # The effect is done to their ACTIVE (it is the one switched out), so
        # an Omega Barrier Active stays put while an Omega Barrier bencher may
        # still be the one brought up.
        await ctx.switch_active(ctx.opponent_id, target or opp_bench[0],
                                object_is_active=True)
        # Flush the opponent's swap so both clients see it land before the
        # Escape Rope player is prompted for their own switch.
        await ctx.flush_choreography()
    my_bench = ctx.my_bench()
    if my_bench:
        target = await ctx.choose_pokemon(
            my_bench, "Choose your new Active Pokémon", player_id=ctx.player_id
        )
        await ctx.switch_active(ctx.player_id, target or my_bench[0])


async def lost_vacuum(ctx):
    """Lost-Zone a card from hand, then Lost-Zone a Tool in play or the Stadium."""
    cost = await ctx.choose_cards(
        ctx.hand(), 1, prompt="Choose a card to put in the Lost Zone"
    )
    if not cost:
        return
    await ctx.move_to_lost_zone(cost)
    targets = _tools_and_stadium(ctx.board)
    picks = await ctx.choose_cards(
        targets, 1, prompt="Choose a Pokémon Tool or Stadium to put in the Lost Zone",
    )
    await ctx.move_to_lost_zone(picks)


def shuffle_from_discard(predicate, count: int, prompt: str, up_to: bool = False):
    """"Shuffle N <cards> from your discard pile into your deck."

    up_to passes minimum=0, letting the player stop short of N with more
    still available -- Super Rod's errata'd wording. Without it choose_cards
    takes exactly N, or the whole pile when it cannot supply N, which is what
    a flat "Shuffle N" asks for (Special Charge).
    """
    async def effect(ctx):
        candidates = [c for c in ctx.discard_pile() if predicate(c)]
        if not candidates:
            return
        picks = await ctx.choose_cards(
            candidates, count, minimum=0 if up_to else None, prompt=prompt)
        if picks:
            await ctx.shuffle_into_deck(picks)
    return effect


super_rod = shuffle_from_discard(
    lambda c: bool(pokemon_or_basic_energy([c])), 3,
    "Choose up to 3 Pokémon and/or basic Energy cards to shuffle into your deck.",
    up_to=True,
)

special_charge = shuffle_from_discard(
    is_special_energy, 2,
    "Choose 2 Special Energy cards to shuffle into your deck.",
)


async def field_blower(ctx):
    """Discard up to 2 Pokemon Tools and/or Stadiums in play, either side."""
    targets = _tools_and_stadium(ctx.board)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 2, minimum=1,
        # The client ships its own string for this card; using the key gets
        # the localized wording instead of an English literal.
        prompt="playmat.prompt.sm2_125.fieldblower",
    )
    if picks:
        await ctx.discard_cards(picks)


async def battle_vip_pass(ctx):
    """First turn only: search the deck for up to 2 Basic Pokemon and put
    them onto your Bench."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = BENCH_CAPACITY - len(bench.children) if bench else 0
    count = min(2, space)
    if count <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=count, minimum=0,
        prompt="Choose up to 2 Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


def dream_ball_playable(board, player_id):
    """Dream Ball never plays from hand: its window is the prize-take prompt."""
    return False


async def dream_ball(ctx):
    """Search your deck for a Pokemon and put it onto your Bench."""
    picks = await ctx.search_deck(
        is_pokemon_card, count=1, minimum=0,
        prompt="Choose a Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def dream_ball_prize_window(ctx):
    """Taken as a face-down Prize: you may play it before it settles in hand.

    No Item-lock check, for the same reason as Greedy Dice: the locks all
    say "from their hand" and this is played out of the Prize cards.
    """
    ctx.suppress_announce = True
    board, pid = ctx.board, ctx.player_id
    bench = board.find_player_area(pid, "bench")
    if not bench or len(bench.children) >= effective_bench_capacity(board, pid):
        return
    if not ctx.deck(pid):
        return
    if not await ctx.ask_yes_no("Play Dream Ball? Search your deck for a "
                                "Pokémon and put it onto your Bench."):
        return
    await ctx.session._execute_play_trainer(pid, ctx.source)


def discard_self_tool_at_end_of_turn(card_name: str):
    """"At the end of your turn, discard this card." for a Pokemon Tool
    (the Technical Machines). The Energy version lives in energies.py; this
    one walks the holder's stack instead of its attached Energy.

    The trigger fires on the HOLDER, so the effect has to find its own card
    back among the attachments; matching on the printed name takes every
    copy on that Pokemon and leaves other Tools alone.
    """
    async def effect(ctx):
        holder = ctx.source
        if holder is None:
            return
        to_discard = [
            card for card in full_stack(holder)
            if card is not holder and is_pokemon_tool(card)
            and getattr(def_for(card.archetype_id), "display_name", None)
            == card_name
        ]
        if to_discard:
            await ctx.discard_cards(to_discard)
    return effect


# --- Greedy Dice (STS, Item) ----------------------------------------------

def greedy_dice_playable(board, player_id):
    """Like Dream Ball, it never plays from hand: its window is the
    prize-take prompt."""
    return False


async def greedy_dice(ctx):
    """Flip a coin. If heads, take 1 more Prize card."""
    heads = await ctx.flip_coins(1, "Greedy Dice")
    if heads and heads[0]:
        await ctx.take_prizes(1)


async def greedy_dice_prize_window(ctx):
    """Taken as a face-down Prize: you may play it before it settles in hand.

    No Item-lock check: every Item lock in the pool reads "can't play any
    Item cards FROM THEIR HAND", and this one is played out of the Prize
    cards. Quaking Punch and friends do not stop it.
    """
    ctx.suppress_announce = True
    if not await ctx.ask_yes_no(
            "Play Greedy Dice? Flip a coin; if heads, take 1 more Prize card."):
        return
    await ctx.session._execute_play_trainer(ctx.player_id, ctx.source)


async def power_tablet(ctx):
    """This turn, your Fusion Strike Pokemon's attacks do 30 more damage to
    the opponent's Active Pokemon (before Weakness and Resistance)."""
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(30, ctx.player_id, requires_subtype="Fusion Strike")
    )
    # Green up-arrow PiP on each buffed Fusion Strike Pokemon in play.
    for pokemon in ctx.my_pokemon_in_play():
        if "Fusion Strike" in subtypes_for(pokemon.archetype_id):
            await ctx.add_stat_visualization(
                pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage"
            )


async def cramomatic(ctx):
    """Discard another Item card, then flip a coin; heads searches the deck
    for any card and puts it into your hand."""
    if not await ctx.discard_from_hand(
        1, predicate=is_item_card, prompt="Discard an Item card for Cram-o-matic"
    ):
        return
    heads, = await ctx.flip_coins(1, "Cram-o-matic")
    if not heads:
        return
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def rotom_phone(ctx):
    """Look at the top 5 cards of your deck, choose 1, shuffle the rest back
    into your deck, then put the chosen card on top."""
    top = ctx.deck_top(5)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 1, minimum=1, prompt="Choose a card to put on top of your deck",
    )
    if not picks:
        return
    await ctx.shuffle_deck_below(picks[0])


async def fan_of_waves(ctx):
    """Put a Special Energy attached to 1 of the opponent's Pokemon on the
    bottom of their deck."""
    targets = _opponent_special_energies(ctx.board, ctx.player_id)
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose a Special Energy to put on the bottom of their deck",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


async def star_alchemy(ctx):
    """Search your deck for a card and put it into your hand (VSTAR Power)."""
    picks = await ctx.search_deck(
        None, count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    # No "reveal it" clause on this card's text (unlike Ultra/Quick Ball).
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


# --- Stadiums & Pokemon Tools -------------------------------------------------

class BigParasolPassive(Passive):
    """While the holder is in the Active Spot, shields the owner's whole
    side from the opponent's attack EFFECTS (not damage)."""

    def blocks_attack_effects(self, target, carrier, source=None):
        holder = carrier_pokemon(carrier)
        if holder is None or target.owning_player_id != holder.owning_player_id:
            return False
        parent = holder.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


class PathToThePeakPassive(Passive):
    """Rule Box Pokemon (both sides) have no Abilities."""

    def blocks_abilities(self, pokemon, carrier):
        return has_rule_box(pokemon.archetype_id)


class ShieldedStadiumPassive(Passive):
    """"Whenever any player plays an Item or Supporter card from their hand,
    prevent all effects of that card done to this Stadium card."

    The Prism Star Stadiums (Thunder Mountain, Black Market) print this
    sentence identically, so they share it.
    """

    def blocks_trainer_targeting(self, target, carrier):
        return target is carrier


class ThunderMountainPassive(ShieldedStadiumPassive):
    """Lightning Pokemon's attacks (both sides) cost [L] less."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if not is_pokemon_of_type(pokemon, PokemonTypes.LIGHTNING):
            return cost
        remaining = cost.get("Lightning", 0) - 1
        if remaining > 0:
            cost["Lightning"] = remaining
        else:
            cost.pop("Lightning", None)
        return cost


class WondrousLabyrinthPassive(ShieldedStadiumPassive):
    """Attacks of non-Fairy Pokemon (both sides) cost [C] more."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if is_pokemon_of_type(pokemon, PokemonTypes.FAIRY):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


class BlackMarketPassive(ShieldedStadiumPassive):
    """A Darkness Pokemon with any Darkness Energy attached is worth one
    Prize less when an opponent's attack knocks it out -- either side's."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        # "by damage from an opponent's attack", as Lillie's Pearl reads it.
        if not ctx.is_attack_effect() or ctx.player_id == pokemon.owning_player_id:
            return count
        if not is_pokemon_of_type(pokemon, PokemonTypes.DARKNESS):
            return count
        attached = ctx.board.attached_energies(pokemon)
        if not any(energy_provides_type(e, PokemonTypes.DARKNESS.value)
                   for e in attached):
            return count
        return max(0, count - 1)


class SilentLabPassive(Passive):
    """Basic Pokemon have no Abilities -- in play, in hand and in the discard
    pile, on both sides.

    Garbotoxin's pair of hooks with a different filter and no switch: a
    Stadium is always on, and unlike Klefki's Mischievous Lock there is no
    "except" clause to honour, so every Basic loses its Abilities including
    Klefki's own.
    """

    def blocks_abilities(self, pokemon, carrier):
        # In play a Fossil IS a Basic Pokemon (in hand and in the discard it
        # is an Item, which the out-of-play half below reads correctly).
        return is_basic_pokemon_in_play(pokemon)

    def blocks_out_of_play_abilities(self, card, carrier):
        return is_basic_pokemon(card)


class LostCityPassive(Passive):
    """Knocked Out Pokemon go to the Lost Zone instead of the discard pile."""

    def knockout_destination(self, pokemon, carrier):
        return "lostZone"


class CollapsedStadiumPassive(Passive):
    """Each player can't have more than 4 Benched Pokemon (excess is discarded
    by enforce_bench_capacity when this comes into play)."""

    def bench_capacity(self, player_id, carrier):
        return 4


async def gapejaw_bog_watch(ctx):
    """Gapejaw Bog: 2 damage counters on any Basic just benched from hand."""
    pokemon = ctx.benched_pokemon
    # "from their hand" -- an effect putting a Basic onto the Bench (Nest
    # Ball) is not a hand play, and the same trigger now carries both.
    if pokemon is None or not getattr(ctx, "benched_from_hand", True):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)


class SkatersParkPassive(Passive):
    """Basic Energy paid for either player's retreat goes to hand instead."""

    def retreat_cost_destination(self, pokemon, energy, carrier):
        return "hand" if is_basic_energy_card(energy) else None


# ======================================================================
# Lost Zone Box + Regigigas decks
# ======================================================================

def is_v_or_gx(archetype_id) -> bool:
    return is_pokemon_v(archetype_id) or "GX" in subtypes_for(archetype_id)


def has_basic_energy_in_discard(board, player_id) -> bool:
    return any(is_basic_energy_card(c) for c in _discard(board, player_id))


def pokemon_or_basic_energy(cards):
    """The "in any combination of Pokemon and basic Energy cards" filter
    (Super Rod, Max Rod)."""
    return [c for c in cards if is_pokemon_card(c) or is_basic_energy_card(c)]


def discard_has(predicate):
    """Condition: the player's discard pile holds a matching card."""
    def check(board, player_id):
        return any(predicate(c) for c in _discard(board, player_id))
    return check


def has_pokemon_or_basic_energy_in_discard(board, player_id) -> bool:
    return bool(pokemon_or_basic_energy(_discard(board, player_id)))


# --- Colress's Experiment (LOR, Supporter) -------------------------------

async def colresss_experiment(ctx):
    """Look at the top 5 cards of your deck, put 3 into your hand, and put the
    other cards in the Lost Zone."""
    top = ctx.deck_top(5)
    if not top:
        return
    take = min(3, len(top))
    picks = await ctx.choose_cards(
        top, take, minimum=take, prompt="Choose 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.move_to_lost_zone([c for c in top if c not in picks])


# --- Klara (CRE, Supporter) ----------------------------------------------

async def klara(ctx):
    """Choose 1 or both: up to 2 Pokemon and/or up to 2 basic Energy from your
    discard pile into your hand."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon from your discard pile.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy from your discard pile.",
    ) if energy else []
    await ctx.put_in_hand(picks_p + picks_e, reveal=False)


# --- Mirage Gate (LOR, Item) ---------------------------------------------

def mirage_gate_condition(board, player_id):
    """Usable only with 7 or more cards in the Lost Zone."""
    lost = board.find_player_area(player_id, "lostZone")
    return bool(lost) and len(lost.children) >= 7


async def mirage_gate(ctx):
    """Search your deck for up to 2 basic Energy of different types and attach
    them to your Pokemon in any way you like. Then, shuffle your deck."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    labels = {}
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
        labels[card.entity_id] = f"{CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(types[0])]} Energy"

    if not reps:
        await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards of different types.",
        )
        await ctx.shuffle_deck()
        return

    picks = await ctx.choose_cards(
        reps, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    for energy in picks:
        label = labels[energy.entity_id]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


# --- Scoop Up Net (RCL, Item) --------------------------------------------

async def scoop_up_net(ctx):
    """Put 1 of your Pokemon that isn't a Pokemon V or GX into your hand.
    Discard all attached cards."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if not is_v_or_gx(p.archetype_id)]
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your Pokémon to put into your hand"
    )
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.discard_cards([c for c in full_stack(target) if c is not target])
    await ctx.put_in_hand([target], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


# --- Acerola / Penny / Professor Turo's Scenario --------------------------

async def _bounce_to_hand(ctx, candidates, prompt, attached_to_hand: bool):
    """Put 1 of your Pokemon into your hand, with the cards attached to it
    following it there (Acerola, Penny) or discarded (Professor Turo's
    Scenario, Scoop Up Net).

    The attached cards move FIRST either way: moving the Pokemon takes its
    children with it, and a card that rode along would sit in the hand still
    attached to it.
    """
    target = await ctx.choose_pokemon(candidates, prompt)
    if target is None:
        return
    was_active = target is ctx.my_active()
    attached = [c for c in full_stack(target) if c is not target]
    if attached_to_hand:
        await ctx.put_in_hand(attached, reveal=False)
    else:
        await ctx.discard_cards(attached)
    await ctx.put_in_hand([target], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


def _damaged_pokemon(board, pokemon) -> bool:
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def acerola_condition(board, player_id) -> bool:
    return any(_damaged_pokemon(board, p) for p in board.pokemon_in_play(player_id))


async def acerola(ctx):
    """Put 1 of your damaged Pokemon and everything attached to it into your
    hand. Damage counters are not "attached cards" -- the Pokemon simply
    leaves play, and comes back as a fresh card."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if _damaged_pokemon(ctx.board, p)]
    await _bounce_to_hand(
        ctx, candidates,
        "Choose 1 of your damaged Pokémon to put into your hand",
        attached_to_hand=True)


def penny_condition(board, player_id) -> bool:
    return any(p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
               for p in board.pokemon_in_play(player_id))


async def penny(ctx):
    """Put 1 of your Basic Pokemon and everything attached to it into your
    hand. A Basic sitting UNDER an evolution is not "your Basic Pokemon" --
    the Pokemon in play is the top card."""
    candidates = [p for p in ctx.my_pokemon_in_play()
                  if p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value]
    await _bounce_to_hand(
        ctx, candidates,
        "Choose 1 of your Basic Pokémon to put into your hand",
        attached_to_hand=True)


async def professor_turos_scenario(ctx):
    """Put 1 of your Pokemon in play into your hand; everything attached to
    it is discarded. Any of them, evolved ones included -- the whole stack
    goes back, so a Stage 2 returns as the single card it was played as."""
    await _bounce_to_hand(
        ctx, list(ctx.my_pokemon_in_play()),
        "Choose 1 of your Pokémon to put into your hand",
        attached_to_hand=False)


# --- Cyrus {*} (UPR, Supporter, Prism Star) -------------------------------

def cyrus_prism_condition(board, player_id) -> bool:
    """Playable only with a [W] or [M] Active."""
    active = board.active_pokemon(player_id)
    return active is not None and (
        is_pokemon_of_type(active, PokemonTypes.WATER)
        or is_pokemon_of_type(active, PokemonTypes.METAL)
    )


async def cyrus_prism_star(ctx):
    """Your opponent chooses 2 of their Benched Pokemon; the rest, and
    everything attached to them, are shuffled into their deck.

    THEY choose, so the prompt is theirs -- and with 2 or fewer on the Bench
    there is nothing to lose, which is why the card is worth playing only
    into a wide board.
    """
    bench = list(ctx.opponent_bench())
    if len(bench) <= 2:
        return
    kept = await ctx.choose_cards(
        bench, 2, minimum=2, player_id=ctx.opponent_id,
        prompt="Choose 2 of your Benched Pokémon to keep.",
    )
    kept_ids = {p.entity_id for p in kept}
    leaving = [c for p in bench if p.entity_id not in kept_ids
               for c in full_stack(p)]
    if leaving:
        await ctx.shuffle_into_deck(leaving, ctx.opponent_id)


# --- Roxie (CEC, Supporter) ----------------------------------------------

def _is_gx_or_uppercase_ex(card) -> bool:
    return any(s in ("GX", "EX") for s in subtypes_for(card.archetype_id))


def _roxie_fodder(card) -> bool:
    """A Pokemon card that is neither a Pokemon-GX nor a Pokemon-EX.

    The SM-era pair, so a Scarlet & Violet Pokemon ex (lowercase) is not
    excluded -- it is not a "Pokemon-EX" any more than a V is.
    """
    return is_pokemon_card(card) and not _is_gx_or_uppercase_ex(card)


def roxie_condition(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(_roxie_fodder(c) for c in (hand.children if hand else []))


async def roxie(ctx):
    """Discard up to 2 non-GX/EX Pokemon from your hand; draw 3 for each.

    The discarded cards then get their own say: "Blow-Away Bomb" fires here
    rather than in the discard path, which is what the card means by
    "(Place damage counters after the effect of Roxie.)".
    """
    discarded = await ctx.discard_from_hand(
        2, minimum=0, predicate=_roxie_fodder,
        prompt="Discard up to 2 Pokémon that aren't Pokémon-GX or Pokémon-EX.")
    if not discarded:
        return
    await ctx.draw_cards(3 * len(discarded))
    for card in discarded:
        await ctx.session._fire_triggered_abilities(
            ctx.player_id, card, Triggers.ON_DISCARDED_BY_ROXIE)


async def blow_away_bomb(ctx):
    """A damage counter on each of their Pokemon, if you want it."""
    targets = list(ctx.opponent_pokemon_in_play())
    if not targets:
        return
    if not await ctx.ask_yes_no(
            "Put 1 damage counter on each of your opponent's Pokémon?"):
        return
    for target in targets:
        await ctx.deal_damage(10, target=target, as_counters=True,
                              apply_modifiers=False)


# --- Fire-deck engine pieces (Fiery Flint, Wait and See Hammer, Archie's,
#     Brigette, Will, Eri, Electropower) ----------------------------------

def is_fire_energy_card(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.FIRE)


def is_fire_or_fighting_energy_card(card) -> bool:
    return (is_energy_of_type(card, PokemonTypes.FIRE)
            or is_energy_of_type(card, PokemonTypes.FIGHTING))


def is_basic_water_or_fighting_pokemon(card) -> bool:
    return is_basic_pokemon(card) and (
        is_pokemon_of_type(card, PokemonTypes.WATER)
        or is_pokemon_of_type(card, PokemonTypes.FIGHTING))


async def fiery_flint(ctx):
    """Discard 2 other cards, then up to 4 [R] Energy out of the deck."""
    if len(await ctx.discard_from_hand(
            2, prompt="Discard 2 cards for Fiery Flint")) < 2:
        return
    picks = await ctx.search_deck(
        is_fire_energy_card, count=4, minimum=0,
        prompt="Choose up to 4 Fire Energy cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def second_players_first_turn(board, player_id, pokemon=None) -> bool:
    """"Only if you go second, and only on your first turn" is turn 2 of
    the game (Shaymin ASR 14, Scatterbug FLI 5 read it the same way)."""
    return board.turn_state.turn_number == 2


def wait_and_see_hammer_condition(board, player_id, pokemon=None) -> bool:
    opponent = _other_player(board, player_id)
    return second_players_first_turn(board, player_id) and opponent is not None \
        and any(board.attached_energies(p) for p in board.pokemon_in_play(opponent))


async def wait_and_see_hammer(ctx):
    """An Energy off 1 of their Pokemon -- any of them, Bench included."""
    targets = [p for p in ctx.opponent_pokemon_in_play()
               if ctx.attached_energies(p)]
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon to discard an Energy from")
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1, prompt="Choose an Energy to discard")


def archies_ace_condition(board, player_id, pokemon=None) -> bool:
    """The last card in hand, a [W] Pokemon in the discard, room on the Bench."""
    hand = board.find_player_area(player_id, "hand")
    if not hand or len(hand.children) != 1:
        return False
    discard = board.find_player_area(player_id, "discard")
    if not any(is_water_pokemon(c) for c in (discard.children if discard else [])):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and len(bench.children) < effective_bench_capacity(board, player_id)


async def archies_ace_in_the_hole(ctx):
    """A [W] Pokemon -- any stage -- from the discard onto the Bench, then 5."""
    candidates = [c for c in ctx.discard_pile() if is_water_pokemon(c)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Water Pokémon to put onto your Bench.")
    if not picks:
        return
    if not await ctx.bench_pokemon(picks[0]):
        return
    await ctx.draw_cards(5)


def _is_basic_ex(card) -> bool:
    return is_basic_pokemon(card) and "EX" in subtypes_for(card.archetype_id)


def _is_basic_non_ex(card) -> bool:
    return is_basic_pokemon(card) and "EX" not in subtypes_for(card.archetype_id)


async def brigette(ctx):
    """1 Basic Pokemon-EX, or 3 Basic Pokemon that are not EX, onto the Bench.

    The choice is made up front, as the card reads it; each search is capped
    by the Bench space actually left."""
    choice = await ctx.choose(
        "Brigette: which will you search for?",
        ["1 Basic Pokémon-EX", "3 Basic Pokémon (not EX)"])
    predicate, count = ((_is_basic_ex, 1) if choice == 0
                        else (_is_basic_non_ex, 3))
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    take = min(count, space)
    if take > 0:
        picks = await ctx.search_deck(
            predicate, count=take, minimum=0,
            prompt="Choose Basic Pokémon to put onto your Bench.")
        for card in picks:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


async def will(ctx):
    """Choose heads or tails for the first coin of your next flip this turn."""
    choice = await ctx.choose("Will: choose the result of your next first coin flip.",
                              ["Heads", "Tails"])
    ctx.session.turn_state.forced_first_flip = (choice == 0)


def eri_condition(board, player_id, pokemon=None) -> bool:
    opponent = _other_player(board, player_id)
    hand = board.find_player_area(opponent, "hand") if opponent else None
    return bool(hand and hand.children)


async def eri(ctx):
    """They reveal their hand; up to 2 Item cards from it are discarded."""
    hand = await ctx.reveal_hand(ctx.opponent_id)
    items = [c for c in hand if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(
        items, 2, minimum=0,
        prompt="Choose up to 2 Item cards to discard from your opponent's hand.")
    if picks:
        await ctx.discard_cards(picks)


async def electropower(ctx):
    """This turn, your [L] Pokemon's attacks do 30 more to their Active."""
    def _is_lightning(pokemon):
        return is_pokemon_of_type(pokemon, PokemonTypes.LIGHTNING)
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(30, ctx.player_id, source_predicate=_is_lightning))
    for pokemon in ctx.my_pokemon_in_play():
        if _is_lightning(pokemon):
            await ctx.add_stat_visualization(
                pokemon, "Positive", "DamageDealtIncreased", card_text="+30 damage")


# --- Switch Cart (ASR, Item) ---------------------------------------------

def switch_cart_condition(board, player_id):
    active = board.active_pokemon(player_id)
    return (
        active is not None
        and active.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
        and bool(_bench_pokemon(board, player_id))
    )


async def switch_cart(ctx):
    """Switch your Active Basic Pokemon with a Benched Pokemon; heal 30 from
    the Pokemon you moved to the Bench."""
    active = ctx.my_active()
    bench = ctx.my_bench()
    if active is None or not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    await ctx.heal(30, active)


# --- Ordinary Rod (SSH, Item) --------------------------------------------

async def ordinary_rod(ctx):
    """Choose 1 or both: shuffle up to 2 Pokemon and/or up to 2 basic Energy
    from your discard pile into your deck."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    picks_p = await ctx.choose_cards(
        pokemon, 2, minimum=0,
        prompt="Choose up to 2 Pokémon to shuffle into your deck.",
    ) if pokemon else []
    picks_e = await ctx.choose_cards(
        energy, 2, minimum=0,
        prompt="Choose up to 2 basic Energy to shuffle into your deck.",
    ) if energy else []
    picks = picks_p + picks_e
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Energy Recycler (BST, Item) -----------------------------------------

async def energy_recycler(ctx):
    """Shuffle up to 5 basic Energy cards from your discard pile into your deck."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 5, minimum=1,
        prompt="Choose up to 5 basic Energy to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


# --- Trekking Shoes (ASR, Item) ------------------------------------------

async def trekking_shoes(ctx):
    """Look at the top card of your deck; you may put it into your hand,
    otherwise discard it and draw a card."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Put this card into your hand?",
        ["Put into hand", "Discard and draw a card"],
    )
    if idx == 0:
        await ctx.put_in_hand([card], reveal=False)
    else:
        await ctx.discard_cards([card])
        await ctx.draw_cards(1)


# --- Hisuian Heavy Ball (ASR, Item) --------------------------------------

def has_face_down_prize(board, player_id, pokemon=None) -> bool:
    """Playability for the cards that LOOK AT your face-down Prize cards
    (Hisuian Heavy Ball, Beast Ball, Gladion).

    Every clause of those cards names FACE-DOWN Prizes, so with none left
    face down there is nothing to look at. Town Map turns them all face up;
    cards that flip only some leave the rest playable, which is why this
    counts rather than asking whether Town Map was played.
    """
    area = board.find_player_area(player_id, "prizePile")
    return any(not c.face_up for c in (area.children if area else []))


def is_ultra_beast(card) -> bool:
    return is_pokemon_card(card) and "Ultra Beast" in subtypes_for(card.archetype_id)


async def beast_ball(ctx):
    """Look at your face-down Prize cards; you MAY reveal an Ultra Beast
    there, put it into your hand, and put this card in its place.

    Hisuian Heavy Ball with a different filter -- the swap, the re-hide and
    the shuffle are the same, so both go through look_at_prizes_take.
    """
    await ctx.look_at_prizes_take(
        predicate=is_ultra_beast,
        prompt="You may reveal an Ultra Beast among your Prize cards.")


async def hisuian_heavy_ball(ctx):
    """Look at your face-down Prize cards; you MAY reveal a Basic Pokemon
    there, put it into your hand, and put this card in its place as a
    face-down Prize. Then shuffle your face-down Prize cards. (No Basic
    revealed -> discard normally.)

    The prize-fan node keeps the client's peek-your-prizes click handler
    suppressed; the reveal browser did not, which crashed on prize clicks."""
    await ctx.look_at_prizes_take(predicate=is_basic_pokemon)


async def gladion(ctx):
    """Look at your face-down Prize cards and put 1 of them into your hand.
    Then shuffle this card into the remaining face-down Prizes.

    Hisuian Heavy Ball with the two knobs turned: any Prize card rather than
    only a Basic, and mandatory rather than "you may". The swap and shuffle
    are identical, which is why both go through look_at_prizes_take.

    "If you didn't play this Gladion from your hand, it does nothing" is the
    anti-copy clause; a Supporter effect only ever runs from a hand play
    here, so there is nothing to gate."""
    await ctx.look_at_prizes_take(minimum=1, prompt=PROMPT_CHOOSE_A_PRIZE)


# --- Peonia (CRE, Supporter) ----------------------------------------------

def peonia_playable(board, player_id) -> bool:
    prizes = board.find_player_area(player_id, "prizePile")
    return bool(prizes and prizes.children)


async def peonia(ctx):
    """Put up to 3 Prize cards into your hand. Then, for each Prize card put
    into your hand this way, put a card from your hand face down as a Prize.

    "Put into your hand", not "take": Jirachi {*}, Dream Ball and Greedy
    Dice get no window here (official ruling), the same as Gladion."""
    taken = await ctx.take_prizes(3, minimum=1, check_win=False,
                                  opens_window=False)
    if not taken:
        return
    picks = await ctx.choose_cards(
        list(ctx.hand()), len(taken), minimum=len(taken),
        prompt=f"Choose {len(taken)} card(s) to put face down as Prize cards",
    )
    await ctx.put_in_prizes(picks)


# --- Escape Board (UPR, Pokemon Tool) ------------------------------------

class EscapeBoardPassive(Passive):
    """The holder's Retreat Cost is [C] less, and it can retreat even while
    Asleep or Paralyzed.

    The second half is a permission, not a cost: the retreat still has to be
    paid for, and the Special Condition itself stays on the Pokemon (a
    retreat cures it the ordinary way, by leaving the Active spot).
    """

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            return cost - 1
        return cost

    def retreats_despite_conditions(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


# --- U-Turn Board (UNM, Pokemon Tool) ------------------------------------

class UTurnBoardPassive(Passive):
    """The holder's Retreat Cost is [C] less, and this card goes back to its
    owner's hand instead of the discard pile when it is discarded from play.

    "Discarded from play" is the whole clause: a copy discarded out of a hand
    (Ultra Ball) or milled from a deck is not in play and goes to the discard
    like anything else, which is why the destination is asked of the card
    only while it is attached.
    """

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            return cost - 1
        return cost

    def discard_destination(self, card, carrier):
        return "hand" if card is carrier else None


# --- Air Balloon (SSH, Pokemon Tool) -------------------------------------

class AirBalloonPassive(Passive):
    """The Retreat Cost of the holder is [C][C] less."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is pokemon:
            return cost - 2
        return cost


# --- Memory Capsule (SWSH4) ------------------------------------------------

class MemoryCapsulePassive(Passive):
    """The holder can use any attack from its tucked previous Evolutions
    (energy costs still apply)."""

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        attacks = []
        for child in pokemon.children:
            if not isinstance(child, PokemonEntity):
                continue
            for ability in getattr(def_for(child.archetype_id), "abilities", None) or []:
                if isinstance(ability, Attack):
                    attacks.append(ability)
        return attacks


# --- Training Court (RCL, Stadium) ---------------------------------------

def training_court_condition(board, player_id, stadium):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_basic_energy_card(c) for c in discard.children)


async def training_court(ctx):
    """Put a basic Energy card from your discard pile into your hand."""
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Energy card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)


# --- Thorton (SWSH11) -------------------------------------------------------

def _basic_pokemon_in_play(board, player_id):
    """In-play Basics; fossils count (Basic Pokemon in play, Trainer CARD_TYPE)."""
    from spirit.game.attributes import AttrID, PokemonStage
    from spirit.game.models.board import PokemonEntity
    return [
        p for p in board.pokemon_in_play(player_id)
        if isinstance(p, PokemonEntity)
        and p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
    ]


def thorton_condition(board, player_id):
    if not any(is_basic_pokemon(c) for c in _discard(board, player_id)):
        return False
    return bool(_basic_pokemon_in_play(board, player_id))


async def thorton(ctx):
    """Choose a Basic Pokemon in your discard pile and switch it with 1 of
    your Basic Pokemon in play; everything remains on the new Pokemon."""
    candidates = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    in_play = _basic_pokemon_in_play(ctx.board, ctx.player_id)
    if not candidates or not in_play:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        in_play, "Choose 1 of your Basic Pokémon in play to switch it with")
    if target is not None:
        await ctx.identity_swap(target, picks[0], destination="discard")


TRAINING_COURT_ABILITY = Ability(
    title="Training Court",
    game_text="Once during each player's turn, that player may put a basic Energy card from their discard pile into their hand.",
    activation=Activations.ONCE_PER_TURN,
    effect=training_court,
    condition=training_court_condition,
)


# --- Fossils (Unidentified Fossil / Rare Fossil) ---------------------------

class FossilBodyPassive(Passive):
    """Fossil rules text: this card can't retreat; Rare Fossil additionally
    can't be affected by Special Conditions."""

    def __init__(self, blocks_conditions: bool = False):
        self.condition_immune = blocks_conditions

    def blocks_retreat(self, pokemon, carrier):
        return pokemon is carrier

    def blocks_special_conditions(self, target, condition, carrier):
        return self.condition_immune and target is carrier


async def fossil_discard(ctx):
    """Discard this fossil from play; attached cards go to the discard too."""
    fossil = ctx.source
    was_active = fossil is ctx.my_active()
    discard = ctx.board.find_player_area(ctx.player_id, "discard")
    if discard is not None and discard.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(discard.entity_id)
    await ctx.discard_cards([c for c in full_stack(fossil) if c is not fossil])
    await ctx.discard_cards([fossil])
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


def fossil_discard_ability() -> Ability:
    """"At any time during your turn, you may discard this card from play."
    Fresh instance per print: ability_id derives from the owning card GUID."""
    return Ability(
        "Discard",
        "At any time during your turn, you may discard this card from play.",
        activation=Activations.ONCE_PER_TURN,
        effect=fossil_discard,
    )


class DollBodyPassive(FossilBodyPassive):
    """The doll rules text: this card can't retreat, and knocking it out is
    worth no Prize at all (Robo Substitute, Lillie's Poke Doll).

    The no-Prize half returns 0 rather than subtracting, because the card
    says the opponent takes NO Prize card for it -- an effect that would
    otherwise add one (Greed Crush, Sky Seal Stone) is adding to zero.
    """

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        return 0 if pokemon is carrier else count


async def doll_to_bottom_of_deck(ctx):
    """Lillie's Poke Doll: from the Active spot, shed everything attached and
    go to the bottom of the deck; a new Active is promoted after."""
    doll = ctx.source
    if doll is None or not is_in_active_spot(doll):
        return
    attached = [c for c in full_stack(doll) if c is not doll]
    if attached:
        await ctx.discard_cards(attached)
    if not await ctx.put_on_bottom_of_deck(doll):
        return

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokemon left"
            )
    ctx.deferred_actions.append(_promote)


def doll_bottom_of_deck_ability() -> Ability:
    """"if this Pokemon is your Active Pokemon, you may discard all cards
    from it and put it on the bottom of your deck." Fresh instance per print:
    ability_id derives from the owning card GUID."""
    return Ability(
        "Return to Deck",
        "At any time during your turn (before your attack), if this Pokemon is "
        "your Active Pokemon, you may discard all cards from it and put it on "
        "the bottom of your deck.",
        activation=Activations.ONCE_PER_TURN,
        condition=lambda board, player_id, pokemon=None: (
            pokemon is not None and board.active_pokemon(player_id) is pokemon),
        effect=doll_to_bottom_of_deck,
    )


def is_rare_fossil(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Rare Fossil"


def bench_has_room(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return bench is not None \
        and len(bench.children) < effective_bench_capacity(board, player_id)


# --- Brandon (SWSH12) -------------------------------------------------------

def brandon_playable(board, player_id) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) == 1


async def brandon(ctx):
    """Draw a card for each Benched Pokemon (both yours and your opponent's)."""
    count = len(_bench_pokemon(ctx.board, ctx.player_id)) \
        + len(_bench_pokemon(ctx.board, ctx.opponent_id))
    if count > 0:
        await ctx.draw_cards(count)


# --- Candice (SWSH12) --------------------------------------------------------

def is_water_energy_card(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.WATER.value in types


def candice_predicate(card) -> bool:
    return is_water_pokemon(card) or is_water_energy_card(card)


# --- Capturing Aroma (SWSH12) ------------------------------------------------

async def capturing_aroma(ctx):
    """Flip a coin: heads searches for an Evolution Pokemon, tails a Basic
    Pokemon; reveal it and put it into your hand. Then, shuffle your deck."""
    heads, = await ctx.flip_coins(1, "Capturing Aroma")
    predicate = is_evolution_pokemon if heads else is_basic_pokemon
    prompt = "Choose an Evolution Pokémon to put into your hand." if heads \
        else "Choose a Basic Pokémon to put into your hand."
    picks = await ctx.search_deck(predicate, count=1, minimum=0, prompt=prompt)
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


# --- Earthen Seal Stone (SWSH12) ---------------------------------------------

async def star_gravity(ctx):
    """Put damage counters on each of the opponent's Pokemon V until its
    remaining HP is 100 (VSTAR Power)."""
    for pokemon in ctx.opponent_pokemon_in_play():
        if not is_pokemon_v(pokemon.archetype_id):
            continue
        current = pokemon.get_attribute(AttrID.HP, ctx.max_hp(pokemon))
        if current > 100:
            await ctx.deal_damage(current - 100, target=pokemon,
                                  apply_modifiers=False, as_counters=True)


# --- Emergency Jelly (SWSH12) -------------------------------------------------

async def emergency_jelly(ctx):
    """End of each turn: if the holder has 30 HP or less remaining and any
    damage counters on it, heal 120 damage from it and discard this card."""
    pokemon = ctx.source
    hp = pokemon.get_attribute(AttrID.HP, 0)
    max_hp = ctx.max_hp(pokemon)
    if hp <= 30 and hp < max_hp:
        await ctx.heal(120, target=pokemon)
        tool = next((t for t, p in ctx.tools_in_play() if p is pokemon), None)
        if tool is not None:
            await ctx.discard_cards([tool])


# --- Furisode Girl (SWSH12) ---------------------------------------------------

async def furisode_girl(ctx):
    """Search the deck for a Basic Pokemon and put it onto the Bench; then
    shuffle. You may switch that Pokemon with your Active Pokemon."""
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    if not picks:
        await ctx.shuffle_deck()
        return
    target = picks[0]
    await ctx.bench_pokemon(target)
    await ctx.shuffle_deck()
    if await ctx.ask_yes_no("Switch that Pokémon with your Active Pokémon?"):
        await ctx.switch_active(ctx.player_id, target)


# --- Lance (SWSH12) -----------------------------------------------------------

def is_dragon_pokemon(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.DRAGON.value in types


async def lance(ctx):
    """Search the deck for up to 3 Dragon Pokemon, reveal them, and put them
    into your hand. Then, shuffle your deck."""
    picks = await ctx.search_deck(
        is_dragon_pokemon, count=3, minimum=0,
        prompt="Choose up to 3 Dragon Pokémon to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


# --- Leafy Camo Poncho (SWSH12) -----------------------------------------------

def leafy_camo_poncho_protects(affected_entity, carrier):
    holder = carrier_pokemon(carrier)
    return holder is not None and affected_entity is holder


def leafy_camo_poncho_condition(board, carrier):
    holder = carrier_pokemon(carrier)
    if holder is None:
        return False
    subs = subtypes_for(holder.archetype_id)
    return "VSTAR" in subs or "VMAX" in subs


# --- Primordial Altar (SWSH12) ------------------------------------------------

def primordial_altar_condition(board, player_id, stadium):
    return deck_nonempty(board, player_id)


async def primordial_altar(ctx):
    """Once during each player's turn: look at the top card of the deck and
    may discard it."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    idx = await ctx.present_card_choice(
        card, "Discard the top card of your deck?",
        ["Discard", "Keep it on top"],
    )
    if idx == 0:
        await ctx.discard_cards([card])


PRIMORDIAL_ALTAR_ABILITY = Ability(
    title="Primordial Altar",
    game_text="Once during each player's turn, that player may look at the top card of their deck. They may discard that card.",
    activation=Activations.ONCE_PER_TURN,
    effect=primordial_altar,
    condition=primordial_altar_condition,
)


# --- Professor Laventon (SWSH12) ----------------------------------------------

def _is_hisuian_pokemon(card) -> bool:
    if not is_pokemon_card(card):
        return False
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return "Hisuian" in name


def professor_laventon_playable(board, player_id) -> bool:
    return any(_is_hisuian_pokemon(c) for c in _discard(board, player_id))


async def professor_laventon(ctx):
    """Put up to 3 Pokemon that have "Hisuian" in their names from the
    discard pile into your hand."""
    candidates = [c for c in ctx.discard_pile() if _is_hisuian_pokemon(c)]
    picks = await ctx.choose_cards(
        candidates, 3, minimum=0,
        prompt="Choose up to 3 Hisuian Pokémon from your discard pile.",
    )
    await ctx.put_in_hand(picks, reveal=False)


# --- Quad Stone (SWSH12) -------------------------------------------------------

async def quad_stone(ctx):
    """Use 1: heal 10 from your Active. Use 4 at once (this + 3 more from
    hand): heal all damage from each of your Pokemon."""
    others = [c for c in ctx.hand()
              if c is not ctx.source and c.archetype_id == ctx.source.archetype_id]
    use_four = False
    if len(others) >= 3 and await ctx.ask_yes_no(
        "Use 3 more Quad Stone cards from your hand to heal all damage from "
        "each of your Pokémon instead of healing 10 from your Active Pokémon?"
    ):
        picks = await ctx.choose_cards(
            others, 3, minimum=3, prompt="Choose 3 more Quad Stone cards to use",
        )
        if len(picks) >= 3:
            await ctx.discard_cards(picks)
            for pokemon in ctx.my_pokemon_in_play():
                await ctx.heal(9999, pokemon)
            use_four = True
    if not use_four:
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(10, active)


# --- Wallace (SWSH12) ----------------------------------------------------------

async def wallace(ctx):
    """Draw 3 cards. Your opponent may draw a card; if they do, draw 1 more."""
    await ctx.draw_cards(3)
    if await ctx.ask_yes_no("Draw a card?", player_id=ctx.opponent_id):
        await ctx.draw_cards(1, ctx.opponent_id)
        await ctx.draw_cards(1)


def fossil_search(fossil_predicate, count: int = 2,
                  label: str = "Rare Fossil"):
    """Search your deck for up to `count` matching fossil cards and put them
    onto your Bench; then shuffle (Relicanth's Fossil Search, Cara Liss)."""
    async def effect(ctx):
        bench = ctx.board.find_player_area(ctx.player_id, "bench")
        space = effective_bench_capacity(ctx.board, ctx.player_id) \
            - len(bench.children) if bench else 0
        if space <= 0:
            return
        picks = await ctx.search_deck(
            fossil_predicate, count=min(count, space), minimum=0,
            prompt=f"Choose up to {min(count, space)} {label} cards to put "
                   f"onto your Bench.",
        )
        for card in picks:
            await ctx.bench_pokemon(card)
        await ctx.shuffle_deck()
    return effect
