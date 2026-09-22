"""Seismitoad-EX (XY - Furious Fists 20/111 -- JP XY3 020/096, the art here).

Basic Water Pokemon-EX. HP 180, weakness Grass x2, retreat 3.

  Quaking Punch   [WC] 30    Your opponent can't play any Item cards from
                             their hand during their next turn.
  Grenade Hammer  [WCCC] 130 This attack does 30 damage to 2 of your
                             Benched Pokemon. (Don't apply Weakness and
                             Resistance for Benched Pokemon.)

The Item lock is the pool's ordinary play lock; Grenade Hammer's recoil
hits MY Bench, and I choose which two.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_item_card

BENCH_HIT = 30
BENCH_TARGETS = 2


async def quaking_punch(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_item_card)


async def grenade_hammer(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    count = min(BENCH_TARGETS, len(bench))
    picks = await ctx.choose_cards(
        bench, count, minimum=count,
        prompt="Choose 2 of your Benched Pokémon to take 30 damage")
    for target in picks:
        await ctx.deal_damage(BENCH_HIT, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="c66eadeb-89ba-568a-a307-372cdb7b051d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SeismitoadEX.Name",
    display_name="Seismitoad-EX",
    searchable_by=["Seismitoad-EX", "Basic", "EX", "SeismitoadEX"],
    subtypes=["Basic", "EX"],
    collector_number=20,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=537,
    abilities=[
        Attack(
            title="Quaking Punch",
            game_text="Your opponent can't play any Item cards from their hand during their next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=quaking_punch,
        ),
        Attack(
            title="Grenade Hammer",
            game_text="This attack does 30 damage to 2 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=grenade_hammer,
        ),
    ],
)
