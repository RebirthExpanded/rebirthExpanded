"""Trevenant & Dusknoir-GX (SM Black Star Promos SM217 -- JP SM12a 053/173).

Basic Psychic TAG TEAM Pokemon-GX. HP 270, weakness Psychic x2, resistance
Fighting -20, retreat 3.

  Night Watch  [PPP] 150  Choose 2 random cards from your opponent's hand.
                          Your opponent reveals those cards and shuffles
                          them into their deck.
  Pale Moon-GX [PC]       At the end of your opponent's next turn, the
                          Defending Pokemon will be Knocked Out. With 1
                          extra [P] Energy attached, discard all Energy from
                          your opponent's Active Pokemon.

Pale Moon-GX is the pool's first delayed knockout, so the turn state now
carries a schedule (entity -> the turn at whose end it faints) that the
turn loop resolves after the end-of-turn triggers and before the checkup.
Putting it there matters: a Pokemon marked to faint does not heal its way
out at the checkup, and one that has already left play by then --
retreated, scooped up, Knocked Out first -- simply drops off the schedule.

The knockout is an EFFECT, not damage: Prizes are taken the ordinary way,
but nothing watching for attack damage fires for it.

Night Watch takes its two cards at RANDOM, so it does not look at their
hand first; the cards are revealed on the way into the deck, which is what
the player is entitled to see.

The English print is the SM Black Star Promo; the Japanese one is a Cosmic
Eclipse-era set card.
"""

import random

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.legal_actions import attack_cost_satisfied

# The [PC] cost plus the one extra [P], asked as a single question.
_COST_PLUS_EXTRA = {"Psychic": 2, "Colorless": 1}


async def night_watch(ctx):
    """150, then two cards at random out of their hand and into their deck."""
    await ctx.deal_damage()
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = random.sample(list(hand), min(2, len(hand)))
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def pale_moon_gx(ctx):
    """Their Active is marked to faint at the end of their next turn."""
    target = ctx.defender
    if target is not None and not ctx.effects_blocked(target):
        ctx.schedule_knockout(target)
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    active = ctx.opponent_active()
    if active is None or ctx.effects_blocked(active):
        return
    await ctx.discard_energy_from(
        active, 99, prompt="Discard all Energy from the Defending Pokémon")


card = PokemonCardDef(
    guid="40622668-5590-57df-b42f-962db7080306",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantDusknoirGX.Name",
    display_name="Trevenant & Dusknoir-GX",
    searchable_by=["Trevenant & Dusknoir-GX", "Basic", "TAG TEAM", "GX",
                   "TrevenantDusknoirGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=217,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=709,
    abilities=[
        Attack(
            title="Night Watch",
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=150,
            effect=night_watch,
        ),
        Attack(
            title="Pale Moon-GX",
            game_text="At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out. If this Pokémon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), discard all Energy from your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=pale_moon_gx,
        ),
    ],
)
