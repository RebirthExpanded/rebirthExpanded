"""Naganadel & Guzzlord-GX (SM - Cosmic Eclipse 158/236).

Basic Dragon TAG TEAM Pokemon-GX, Ultra Beast. HP 280, weakness Fairy x2,
no resistance, retreat 3.

  Violent Appetite        Ability. Once during your turn (before your
                          attack), you may discard a Pokemon from your hand.
                          If you do, heal 60 damage from this Pokemon.
  Jet Pierce      [PDC] 180
  Chaotic Order-GX  [C]   Turn all of your Prize cards face up. (Those
                          Prize cards remain face up for the rest of the
                          game.) If this Pokemon has at least 1 extra
                          Psychic Energy and 1 extra Darkness Energy
                          attached to it (in addition to this attack's
                          cost), take 2 Prize cards. (You can't use more
                          than 1 GX attack in a game.)

The pool's first TAG TEAM, so data_utils gains "TAG TEAM": 3 beside the
other rule-box subtypes. prize_value takes the max over a card's subtypes,
so this being a GX as well still yields 3, and the subtype joins
_RULE_BOX_SUBTYPES for free, which is right -- a TAG TEAM has a rule box.

Violent Appetite is usable with no damage on the board. The discard is the
COST, not a payment for healing, so nothing gates it on being damaged: the
condition only asks for a Pokemon in hand, and heal() no-ops at full HP.
Playing it undamaged is a legal (if wasteful) way to put a Pokemon in the
discard.

Chaotic Order-GX shares Town Map's ctx.turn_prizes_face_up. The extra-
Energy clause is checked as the whole requirement at once -- cost [C] plus
the extras [P][D] -- through attack_cost_satisfied, which is what "in
addition to this attack's cost" means; a Psychic that is already paying
the [C] cannot also be the extra Psychic.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.legal_actions import attack_cost_satisfied

# Cost plus the extras, asked as one question.
_COST_PLUS_EXTRAS = {"Colorless": 1, "Psychic": 1, "Darkness": 1}


async def violent_appetite(ctx):
    """Discard a Pokemon from hand; if you do, heal 60 from this Pokemon."""
    pokemon_in_hand = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not pokemon_in_hand:
        return
    picks = await ctx.choose_cards(
        pokemon_in_hand, 1, minimum=1,
        prompt="Choose a Pokémon to discard.",
    )
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.heal(60, target=ctx.source)


async def chaotic_order_gx(ctx):
    """Turn your Prizes face up; with an extra [P] and [D] attached, also
    take 2 Prize cards."""
    await ctx.turn_prizes_face_up()
    energies = ctx.attached_energies(ctx.attacker)
    if attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board):
        await ctx.take_prizes(2)


card = PokemonCardDef(
    guid="e38f6251-cb11-5fb6-abf4-d1fabfeed573",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGuzzlordGX.Name",
    display_name="Naganadel & Guzzlord-GX",
    searchable_by=["Naganadel & Guzzlord-GX", "Basic", "TAG TEAM", "GX",
                   "Ultra Beast", "NaganadelGuzzlordGX"],
    subtypes=["Basic", "TAG TEAM", "GX", "Ultra Beast"],
    collector_number=158,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=804,
    abilities=[
        Ability(
            title="Violent Appetite",
            game_text="Once during your turn (before your attack), you may discard a Pokémon from your hand. If you do, heal 60 damage from this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(is_pokemon_card, 1),
            effect=violent_appetite,
        ),
        Attack(
            title="Jet Pierce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1,
                  PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
        Attack(
            title="Chaotic Order-GX",
            game_text="Turn all of your Prize cards face up. (Those Prize cards remain face up for the rest of the game.) If this Pokémon has at least 1 extra Psychic Energy and 1 extra Darkness Energy attached to it (in addition to this attack's cost), take 2 Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            gx=True,
            effect=chaotic_order_gx,
        ),
    ],
)
