"""Gengar & Mimikyu-GX (SM - Team Up 53/181 -- JP SM9 038/095).

Basic Psychic TAG TEAM Pokemon-GX. HP 240, weakness Psychic x2, resistance
Fighting -20, retreat 2.

  Poltergeist    [PP] 50x  Your opponent reveals their hand. This attack
                           does 50 damage for each Trainer card you find
                           there.
  Horror House-GX  [P]+    During your opponent's next turn, your opponent
                           can't play any cards from their hand. If this
                           Pokemon has at least 1 extra Psychic Energy
                           attached to it (in addition to this attack's
                           cost), each player draws cards until they have 7
                           cards in their hand.

Horror House-GX is the widest play lock in the pool: not Items, not
Trainers -- ANY card. It is also the reason legal_actions now asks the
play lock about Pokemon and not only about the fossils, because a lock
that says "any cards" has to stop a Bench play and an evolution as well as
a Supporter.

Energy attachment is a separate action from playing a card, so the lock
does not stop it; the manual attach path reads its own restriction list.

The draw clause fires after the lock and is the "in addition to this
attack's cost" test the pool already uses: cost plus extras asked as one
question through attack_cost_satisfied, so a Psychic already paying the
[P] cannot also be the extra one. Both players draw UP TO 7 -- a player
holding 7 or more draws nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_trainer_card
from spirit.game.session.legal_actions import attack_cost_satisfied

HAND_TARGET = 7
PER_TRAINER = 50
# The [P] cost plus the one extra [P], asked as a single question.
_COST_PLUS_EXTRA = {"Psychic": 2}

def _count_trainers_in_opponent_hand(ctx) -> int:
    return sum(1 for c in ctx.hand(ctx.opponent_id) if is_trainer_card(c))


async def poltergeist(ctx):
    """They show their hand; 50 per Trainer in it."""
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    await damage_per(_count_trainers_in_opponent_hand, PER_TRAINER)(ctx)


async def horror_house_gx(ctx):
    """No cards at all from their hand next turn; with an extra [P], both
    players refill to 7."""
    ctx.lock_plays(ctx.opponent_id, lambda card: True)
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRA, energies, ctx.board):
        return
    for player_id in (ctx.player_id, ctx.opponent_id):
        missing = HAND_TARGET - ctx.hand_size(player_id)
        if missing > 0:
            await ctx.draw_cards(missing, player_id=player_id)


card = PokemonCardDef(
    guid="c6119a7e-7c9d-566c-9a95-c4d8b07e907c",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarMimikyuGX.Name",
    display_name="Gengar & Mimikyu-GX",
    searchable_by=["Gengar & Mimikyu-GX", "Basic", "TAG TEAM", "GX",
                   "GengarMimikyuGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=53,
    set_code="SM9",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=94,
    abilities=[
        Attack(
            title="Poltergeist",
            game_text="Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=poltergeist,
        ),
        Attack(
            title="Horror House-GX",
            game_text="During your opponent's next turn, your opponent can't play any cards from their hand. If this Pokémon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), each player draws cards until they have 7 cards in their hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            gx=True,
            effect=horror_house_gx,
        ),
    ],
)
