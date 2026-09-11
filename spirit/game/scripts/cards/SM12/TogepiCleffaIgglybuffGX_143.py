"""Togepi & Cleffa & Igglybuff-GX (SM - Cosmic Eclipse 143/236 --
JP SM12a 094/173).

Basic Fairy TAG TEAM Pokemon-GX. HP 240, weakness Metal x2, resistance
Darkness -20, retreat 2.

  Rolling Panic    [YYC] 120+  Flip a coin until you get tails. This attack
                               does 30 more damage for each heads.
  Supreme Puff-GX  [YY]        Take another turn after this one. (Skip the
                               between-turns step.) With 14 extra [Y]
                               Energy attached, your opponent shuffles all
                               of their Benched Pokemon and all attached
                               cards into their deck.

The extra turn is Dialga-GX's Timeless-GX: ctx.take_extra_turn(), which the
turn loop consumes by skipping the checkup and dealing the same player
another turn.

The fourteen-Energy clause is nothing special to the engine -- it is the
same "in addition to this attack's cost" question every TAG TEAM asks, with
a large number -- and what it does is a shuffle rather than a discard, so
the Bench goes back into the deck and nothing is Knocked Out.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import full_stack
from spirit.game.session.legal_actions import attack_cost_satisfied

PER_HEADS = 30
# The [YY] cost plus the fourteen extra [Y], asked as a single question.
_COST_PLUS_EXTRAS = {"Fairy": 16}


async def rolling_panic(ctx):
    """120, +30 for every heads before the first tails."""
    heads = await ctx.flip_until_tails("Rolling Panic")
    await ctx.deal_damage(120 + PER_HEADS * heads)


async def supreme_puff_gx(ctx):
    """Another turn; with 14 extra [Y], their Bench goes back into the deck."""
    ctx.take_extra_turn()
    energies = ctx.attached_energies(ctx.attacker)
    if not attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board):
        return
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    cards = [card for pokemon in bench for card in full_stack(pokemon)]
    await ctx.shuffle_into_deck(cards, ctx.opponent_id)


card = PokemonCardDef(
    guid="bbe863c3-d9c7-5e5a-b189-c09cfaf92e42",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TogepiCleffaIgglybuffGX.Name",
    display_name="Togepi & Cleffa & Igglybuff-GX",
    searchable_by=["Togepi & Cleffa & Igglybuff-GX", "Basic", "TAG TEAM", "GX",
                   "TogepiCleffaIgglybuffGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=143,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=175,
    abilities=[
        Attack(
            title="Rolling Panic",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=rolling_panic,
        ),
        Attack(
            title="Supreme Puff-GX",
            game_text="Take another turn after this one. (Skip the between-turns step.) If this Pokémon has at least 14 extra Fairy Energy attached to it (in addition to this attack's cost), your opponent shuffles all of their Benched Pokémon and all cards attached to them into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2},
            gx=True,
            effect=supreme_puff_gx,
        ),
    ],
)
