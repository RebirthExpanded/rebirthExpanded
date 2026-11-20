"""Mega Evolution "Aura Seeker" (JP M7, set M7, Japanese numbering) effects.

English names and texts are provisional translations of the Japanese
cards (no English release yet); the GUIDs come from the M7 number and stay
when the official English text replaces them.
"""
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType
from spirit.game.data_utils import Attack, def_for, has_rule_box, is_pokemon_ex, subtypes_for
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.models.board import board_of
from spirit.game.session.effects import (
    full_stack,
    is_basic_pokemon,
    is_energy_card,
    is_pokemon_card,
    is_pokemon_of_type,
    is_special_energy,
    is_stadium_card,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import (
    Passive,
    TurnDamageModifier,
    carrier_pokemon,
    effective_pokemon_types,
    effective_retreat_cost,
)
from spirit.game.card_effects.attacks_common import has_attack_titled, lock_all_attacks
from spirit.game.card_effects.passives_common import AttackDiscountPassive, is_in_active_spot
from spirit.game.card_effects.trainers import is_basic_energy_card

MAXI = "Maxi's Passion"


# ----------------------------------------------------------------------
# Predicates
# ----------------------------------------------------------------------

def is_mega_ex(card) -> bool:
    """A Mega Evolution Pokemon ex (Mega ... ex and Mega ... Z ex)."""
    if card is None:
        return False
    subs = subtypes_for(card.archetype_id) or []
    return "SV_Mega" in subs and is_pokemon_ex(card.archetype_id)


def _evolved(card) -> bool:
    return card.get_attribute(AttrID.STAGE) not in (PokemonStage.BASIC.value, None)


def _named(card, name) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == name


def _conditions(pokemon) -> int:
    return len(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def _own_stadium(board, player_id) -> bool:
    area = board.find_global_area("activeStadium")
    return any(c.owning_player_id == player_id for c in (area.children if area else []))


async def _condition(ctx, target, *conds):
    for cond in conds:
        await ctx.apply_special_condition(target, cond)


# ----------------------------------------------------------------------
# Grass
# ----------------------------------------------------------------------

def acid_trap_condition(board, player_id, pokemon=None) -> bool:
    return _own_stadium(board, player_id) and board.active_pokemon(
        next(p for p in board.player_ids if p != player_id)) is not None


async def acid_trap(ctx):
    """Victreebel: your Stadium in play -> opponent's Active Poisoned and Burned."""
    target = ctx.opponent_active()
    if target is not None:
        await _condition(ctx, target, SpecialConditions.POISONED, SpecialConditions.BURNED)


async def poison_claws(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


async def assassin_blade(ctx):
    """160 + 50 for each Special Condition on the opponent's Active."""
    defender = ctx.defender
    await ctx.deal_damage(160 + 50 * (_conditions(defender) if defender else 0))


def count_opponent_evolved(ctx) -> int:
    return sum(1 for p in ctx.opponent_pokemon_in_play() if _evolved(p))


def count_opponent_basics(ctx) -> int:
    return sum(1 for p in ctx.opponent_pokemon_in_play() if not _evolved(p))


# ----------------------------------------------------------------------
# Fire
# ----------------------------------------------------------------------

class IllusionPassive(Passive):
    """Ninetales: with exactly 5 cards in your hand, the opponent takes no
    Prize cards when this Pokemon is Knocked Out."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return count
        hand = ctx.board.find_player_area(pokemon.owning_player_id, "hand")
        if hand is not None and len(hand.children) == 5:
            return 0
        return count


async def scorch(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


# ----------------------------------------------------------------------
# Water
# ----------------------------------------------------------------------

async def bubble_beam_paralyze(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Bubble Beam")
    if heads and heads[0] and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


class WaterPumpPassive(Passive):
    """Blastoise: attacks of your [W] Pokemon do +30 to your opponent's
    Benched Pokemon. Doesn't stack with another Water Pump."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        attacker = calc.attacker
        if me is None or attacker is None or not calc.is_attack:
            return
        if attacker.owning_player_id != me.owning_player_id:
            return
        if calc.target.owning_player_id == me.owning_player_id or calc.to_active:
            return
        if "m7_water_pump" in calc.applied_once:
            return
        if PokemonTypes.WATER.value not in effective_pokemon_types(calc.board, attacker):
            return
        calc.applied_once.add("m7_water_pump")
        calc.amount += 30


def _maxis_in_hand(ctx):
    return [c for c in ctx.hand() if _named(c, MAXI)]


async def hot_blooded_head(ctx):
    """Quagsire: you may reveal a Maxi's Passion from your hand for +120."""
    bonus = 0
    cards = _maxis_in_hand(ctx)
    if cards and await ctx.ask_yes_no(f"Reveal {MAXI} from your hand for 120 more damage?"):
        await ctx.reveal_cards(cards[:1])
        bonus = 120
    await ctx.deal_damage(20 + bonus)


async def hustle_screw(ctx):
    """Floatzel ex: reveal any number of Maxi's Passion, +100 each, then
    shuffle the revealed cards into your deck."""
    cards = _maxis_in_hand(ctx)
    picks = []
    if cards:
        picks = await ctx.choose_cards(
            cards, len(cards), minimum=0,
            prompt=f"Reveal any number of {MAXI} (100 more damage each)")
    if picks:
        await ctx.reveal_cards(picks)
    await ctx.deal_damage(40 + 100 * len(picks))
    if picks:
        await ctx.shuffle_into_deck(list(picks), ctx.player_id)


# ----------------------------------------------------------------------
# Lightning
# ----------------------------------------------------------------------

async def welcoming_dance(ctx):
    """Oricorio: look at the opponent's hand, put up to 3 Basic Pokemon from
    it onto their Bench."""
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    basics = [c for c in cards if is_basic_pokemon(c)]
    space = BENCH_CAPACITY - len(ctx.opponent_bench())
    if not basics or space <= 0:
        return
    picks = await ctx.choose_cards(
        basics, min(3, len(basics), space), minimum=0,
        prompt="Put up to 3 Basic Pokémon onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


# ----------------------------------------------------------------------
# Psychic
# ----------------------------------------------------------------------

async def energy_leap(ctx):
    """Xatu: when played from hand to evolve -- look at the opponent's hand
    and attach an Energy card from it to 1 of their Pokemon."""
    if not getattr(ctx, "evolved_from_hand", True):
        return
    cards = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    energies = [c for c in cards if is_energy_card(c)]
    targets = ctx.opponent_pokemon_in_play()
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(energies, 1, minimum=1,
                                   prompt="Choose an Energy card from your opponent's hand")
    if not picks:
        return
    target = await ctx.choose_pokemon(targets, "Choose 1 of your opponent's Pokémon to attach it to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)


async def yoga_power(ctx):
    await ctx.place_damage_counters(3, list(ctx.opponent_pokemon_in_play()))


def _blocks_bloody_fear(card) -> bool:
    return is_special_energy(card) or is_stadium_card(card)


async def bloody_fear(ctx):
    """Mega Absol Z ex: next turn the opponent can't play Special Energy
    or Stadium cards from their hand."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _blocks_bloody_fear)


class MegaProtectorPassive(Passive):
    """Sigilyph ex: prevent all damage done to this Pokemon by attacks from
    the opponent's Mega Evolution Pokemon ex."""

    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        attacker = calc.attacker
        return bool(calc.is_attack and calc.target is me and attacker is not None
                    and attacker.owning_player_id != me.owning_player_id
                    and is_mega_ex(attacker))


async def power_cyclone(ctx):
    """140, then move 1 Energy from this Pokemon to 1 of your Benched Pokemon."""
    await ctx.deal_damage()
    me = ctx.attacker
    energies = ctx.attached_energies(me)
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    pick = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not pick:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to")
    if target is not None:
        await ctx.move_energy(pick[0], target)


async def bewilder(ctx):
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


def count_my_bench_mega_ex(ctx) -> int:
    return sum(1 for p in ctx.my_bench() if is_mega_ex(p))


async def future_sight(ctx):
    """Hatenna: look at the top 3 cards of either player's deck and put
    them back in any order."""
    idx = await ctx.choose("Whose deck do you look at?", ["Your deck", "Your opponent's deck"])
    pid = ctx.opponent_id if idx == 1 else ctx.player_id
    if ctx.deck(pid):
        await ctx.reorder_deck_top(3, player_id=pid)


async def magic_tentacle(ctx):
    """Hatterene: discard the top card of each deck; +100 per Trainer."""
    milled = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, pid)
        if top:
            milled.extend(top)
            await ctx.discard_cards(top)
    trainers = sum(1 for c in milled if is_trainer_card(c))
    await ctx.deal_damage(100 + 100 * trainers)


# ----------------------------------------------------------------------
# Fighting
# ----------------------------------------------------------------------

class TrainedArmPassive(Passive):
    """Machamp: this Pokemon's attack damage ignores Resistance and any
    effects on the opponent's Active Pokemon."""

    def attacks_ignore_target_effects(self, attacker, carrier):
        return attacker is carrier_pokemon(carrier)

    def modify_resistance(self, calc, carrier):
        if calc.is_attack and calc.attacker is carrier_pokemon(carrier):
            calc.resistance_applies = False


async def big_shake(ctx):
    """Whiscash: discard the Stadium in play; if you can't, the attack does nothing."""
    if ctx.stadium_in_play() is None:
        return
    await ctx.discard_stadium()
    await ctx.deal_damage()


async def circle_throw(ctx):
    """Throh: 20, then the opponent switches their Active with a Benched
    Pokemon of their choice."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    defender = ctx.opponent_active()
    if not bench or defender is None or ctx.effects_blocked(defender):
        return
    choice = await ctx.choose_pokemon(bench, "Choose a Pokémon to switch in",
                                      player_id=ctx.opponent_id)
    if choice is not None:
        await ctx.switch_active(ctx.opponent_id, choice)


class GutsFightDiscountPassive(AttackDiscountPassive):
    """Hawlucha: your Pokemon's "Guts Fight" costs [C] less."""
    only_attack_title = "Guts Fight"

    def __init__(self):
        super().__init__(1, self_only=False)


def united_formation_condition(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon) and any(
        "Falinks" in (getattr(def_for(p.archetype_id), "display_name", "") or "")
        for p in board.pokemon_in_play(player_id) if p is not board.active_pokemon(player_id))


async def united_formation(ctx):
    """Falinks: attach a Basic [F] Energy from the deck to each of your
    Benched Pokemon with "Falinks" in its name; shuffle."""
    targets = [p for p in ctx.my_bench()
               if "Falinks" in (getattr(def_for(p.archetype_id), "display_name", "") or "")]
    for target in targets:
        found = await ctx.search_deck(
            lambda c: is_basic_energy_card(c) and is_pokemon_of_type(c, PokemonTypes.FIGHTING),
            count=1, minimum=0, prompt="Choose a Basic Fighting Energy to attach")
        if not found:
            break
        await ctx.attach_energy(found[0], target)
    await ctx.shuffle_deck()


async def dark_strike_combo(ctx):
    """Single Strike Urshifu: you may discard a [D] Energy from it for +140."""
    bonus = 0
    pool = [e for e in ctx.attached_energies(ctx.attacker)
            if is_pokemon_of_type(e, PokemonTypes.DARKNESS) or _provides(e, PokemonTypes.DARKNESS)]
    if pool and await ctx.ask_yes_no("Discard a Darkness Energy from this Pokémon for 140 more damage?"):
        pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Darkness Energy to discard")
        if pick:
            await ctx.discard_cards(pick)
            bonus = 140
    await ctx.deal_damage(120 + bonus)


async def torrential_flurry(ctx):
    """Rapid Strike Urshifu: 120; you may discard a [W] Energy from it to
    also do 40 to each of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    pool = [e for e in ctx.attached_energies(ctx.attacker) if _provides(e, PokemonTypes.WATER)]
    if not pool or not ctx.opponent_bench():
        return
    if not await ctx.ask_yes_no("Discard a Water Energy to do 40 damage to each of your opponent's Benched Pokémon?"):
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Water Energy to discard")
    if not pick:
        return
    await ctx.discard_cards(pick)
    for target in list(ctx.opponent_bench()):
        await ctx.deal_damage(40, target=target)


def _provides(energy, ptype) -> bool:
    from spirit.game.card_effects.pokemon import energy_provides_type
    return energy_provides_type(energy, ptype.value)


# ----------------------------------------------------------------------
# Darkness
# ----------------------------------------------------------------------

async def skill_control(ctx):
    """Malamar: choose 1 attack of the opponent's Active Mega Evolution
    Pokemon ex and use it as this attack."""
    defender = ctx.opponent_active()
    if defender is None or not is_mega_ex(defender):
        return
    candidates = [(defender, a) for a in getattr(def_for(defender.archetype_id), "abilities", None) or []
                  if isinstance(a, Attack)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is None:
        return
    await ctx.use_attack(picked[1])


async def toxic_gem(ctx):
    """Mega Glimmora ex: put damage counters on 2 of the opponent's Pokemon
    until each has 60 HP left."""
    pool = list(ctx.opponent_pokemon_in_play())
    if not pool:
        return
    picks = []
    for _ in range(min(2, len(pool))):
        choice = await ctx.choose_pokemon([p for p in pool if p not in picks],
                                          "Choose a Pokémon to leave at 60 HP")
        if choice is None:
            break
        picks.append(choice)
    for target in picks:
        hp = target.get_attribute(AttrID.HP, 0)
        if hp > 60:
            await ctx.deal_damage(hp - 60, target=target, apply_modifiers=False, as_counters=True)


async def big_spin(ctx):
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


async def heavy_bomber(ctx):
    """Ting-Lu: 250 minus 50 for each Energy in the opponent's Active's
    Retreat Cost."""
    defender = ctx.defender
    cost = effective_retreat_cost(ctx.board, defender) if defender is not None else 0
    await ctx.deal_damage(max(0, 250 - 50 * cost))


# ----------------------------------------------------------------------
# Metal
# ----------------------------------------------------------------------

def aura_seeker_condition(board, player_id, pokemon=None) -> bool:
    return pokemon is not None and is_in_active_spot(pokemon)


async def aura_seeker(ctx):
    """Mega Lucario Z ex: search your deck for a Supporter, reveal it, put it
    into your hand; shuffle."""
    found = await ctx.search_deck(is_supporter_card, count=1, minimum=0,
                                  prompt="Choose a Supporter card")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def dancing_fist(ctx):
    defender = ctx.defender
    bonus = 120 if defender is not None and is_pokemon_ex(defender.archetype_id) else 0
    await ctx.deal_damage(120 + bonus)


class DualTypePassive(Passive):
    """Togedemaru ex: [L] and [M] type while in play."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        out = list(types)
        for t in (PokemonTypes.LIGHTNING.value, PokemonTypes.METAL.value):
            if t not in out:
                out.append(t)
        return out


async def all_out_needle(ctx):
    """180; during your next turn this attack does 60 instead."""
    me = ctx.attacker
    turn = ctx.session.turn_state.turn_number
    weakened = getattr(me, "m7_needle_turn", None) == turn - 2
    await ctx.deal_damage(60 if weakened else 180)
    me.m7_needle_turn = turn


async def long_drive(ctx):
    """Revavroom: 100; discard all Energy from it and do 100 to 1 of the
    opponent's Benched Pokemon."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.discard_cards(list(energies))
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to do 100 damage to")
        if target is not None:
            await ctx.deal_damage(100, target=target)


async def burrow_and_refuel(ctx):
    """Orthworm: switch it with a Benched Pokemon, then attach a Basic [M]
    Energy from your discard pile to it."""
    me = ctx.attacker
    bench = ctx.my_bench()
    if bench:
        choice = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if choice is not None:
            await ctx.switch_active(ctx.player_id, choice)
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)
            and is_pokemon_of_type(c, PokemonTypes.METAL)]
    if pool:
        pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Metal Energy to attach")
        if pick:
            await ctx.attach_energy(pick[0], me)


async def smash_head(ctx):
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.discard_energy_from(ctx.attacker, min(2, len(energies)),
                                      minimum=min(2, len(energies)),
                                      prompt="Choose 2 Energy to discard")


# ----------------------------------------------------------------------
# Dragon
# ----------------------------------------------------------------------

def quivering_wings_condition(board, player_id, pokemon=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return deck is not None and bool(deck.children)


async def quivering_wings(ctx):
    """Vibrava (from hand): discard this card, then look at the top card of
    your deck and put it back."""
    await ctx.discard_cards([ctx.source])
    if ctx.deck():
        await ctx.reorder_deck_top(1, prompt="The top card of your deck")


async def desert_wind(ctx):
    """Flygon: 90; you may shuffle 2 Energy from the opponent's Active into
    their deck."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies or not await ctx.ask_yes_no("Shuffle 2 Energy from your opponent's Active Pokémon into their deck?"):
        return
    picks = await ctx.choose_cards(energies, min(2, len(energies)),
                                   minimum=min(2, len(energies)),
                                   prompt="Choose 2 Energy to shuffle into your opponent's deck")
    if picks:
        await ctx.shuffle_into_deck(list(picks), ctx.opponent_id)


def mill_self_attack(count):
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(count)
        if top:
            await ctx.discard_cards(top)
    return effect


def count_my_dragon_in_discard(ctx) -> int:
    return sum(1 for c in ctx.discard_pile()
               if is_pokemon_card(c) and is_pokemon_of_type(c, PokemonTypes.DRAGON))


async def power_breath(ctx):
    """Drampa: 30; search your deck for a Basic Energy and attach it to 1 of
    your [N] Pokemon; shuffle."""
    await ctx.deal_damage()
    dragons = [p for p in ctx.my_pokemon_in_play()
               if PokemonTypes.DRAGON.value in effective_pokemon_types(ctx.board, p)]
    if dragons:
        found = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                      prompt="Choose a Basic Energy to attach")
        if found:
            target = await ctx.choose_pokemon(dragons, "Choose a Dragon Pokémon to attach it to")
            if target is not None:
                await ctx.attach_energy(found[0], target)
    await ctx.shuffle_deck()


# ----------------------------------------------------------------------
# Colorless
# ----------------------------------------------------------------------

def big_coin_bonanza_condition(board, player_id, pokemon=None) -> bool:
    pay_day = has_attack_titled("Pay Day")
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and sum(
        1 for p in board.pokemon_in_play(player_id) if pay_day(p)) >= 2


async def big_coin_bonanza(ctx):
    await ctx.draw_cards(2)


class SynchroBodyPassive(Passive):
    """Kecleon: also has the types of all your Benched Pokemon while in play."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return types
        board = board_of(pokemon)
        if board is None:
            return types
        out = list(types)
        for other in board.pokemon_in_play(pokemon.owning_player_id):
            if other is pokemon or other is board.active_pokemon(pokemon.owning_player_id):
                continue
            for t in other.get_attribute(AttrID.POKEMON_TYPES) or []:
                if t not in out:
                    out.append(t)
        return out


def _retreat_four(card) -> bool:
    return is_pokemon_card(card) and int(card.get_attribute(AttrID.RETREAT_COST) or 0) == 4


async def stomping_march(ctx):
    found = await ctx.search_deck(_retreat_four, count=3, minimum=0,
                                  prompt="Choose up to 3 Pokémon with a Retreat Cost of 4")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


async def destructive_hammer(ctx):
    """Regigigas: you may discard up to 10 cards from the top of your deck,
    +10 for each."""
    deck_size = len(ctx.deck())
    count = 0
    if deck_size:
        options = [str(n) for n in range(0, min(10, deck_size) + 1)]
        idx = await ctx.choose("Discard how many cards from the top of your deck? (10 more damage each)",
                               options, use_panel=False)
        count = int(options[idx]) if idx is not None and 0 <= idx < len(options) else 0
    if count:
        await ctx.discard_cards(ctx.deck_top(count))
    await ctx.deal_damage(120 + 10 * count)


# ----------------------------------------------------------------------
# Trainers
# ----------------------------------------------------------------------

async def bond_sash(ctx):
    """Tool: when the Mega Evolution Pokemon ex it is attached to is Knocked
    Out by damage from an opponent's attack, search your deck for any card."""
    holder = ctx.source
    if not ctx.ko_from_attack or not is_mega_ex(holder):
        return
    found = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put into your hand")
    if found:
        await ctx.put_in_hand(found, reveal=False)
    await ctx.shuffle_deck()


async def korrinas_determination(ctx):
    """This turn your Mega Evolution Pokemon ex's attacks do +20 to the
    opponent's Active for each Prize card your opponent has taken."""
    taken = ctx.prizes_taken(ctx.opponent_id)
    if taken <= 0:
        return
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount=20 * taken, player_id=ctx.player_id,
        opposing_active_only=True, source_predicate=is_mega_ex))


def maxis_passion_condition(board, player_id, *args) -> bool:
    return any(is_pokemon_of_type(p, PokemonTypes.WATER) for p in board.pokemon_in_play(player_id))


async def maxis_passion(ctx):
    """Shuffle 1 of your [W] Pokemon and all attached cards into your deck."""
    candidates = [p for p in ctx.my_pokemon_in_play() if is_pokemon_of_type(p, PokemonTypes.WATER)]
    target = await ctx.choose_pokemon(candidates, "Choose a Water Pokémon to shuffle into your deck")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(ctx.opponent_id, f"{name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


async def reporter(ctx):
    """Draw 2; look at the opponent's hand; look at the top card of their
    deck and put it back."""
    await ctx.draw_cards(2)
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    if ctx.deck(ctx.opponent_id):
        await ctx.reorder_deck_top(1, player_id=ctx.opponent_id,
                                   prompt="The top card of your opponent's deck")


def fight_arena_condition(board, player_id, stadium=None) -> bool:
    from spirit.game.session.passives import effective_max_hp
    return any(not has_rule_box(p.archetype_id)
               and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in board.pokemon_in_play(player_id))


async def fight_arena(ctx):
    """Once during each player's turn: heal 20 from each of their Pokemon
    that has no Rule Box."""
    for pokemon in ctx.my_pokemon_in_play():
        if not has_rule_box(pokemon.archetype_id):
            await ctx.heal(20, pokemon)
