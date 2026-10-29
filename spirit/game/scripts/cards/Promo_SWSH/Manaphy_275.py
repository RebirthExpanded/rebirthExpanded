"""Manaphy (Promo_SWSH 275 -- JP SP 286; English SP/275). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def _pulling_currents(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    space = effective_bench_capacity(ctx.board, ctx.opponent_id) - len(ctx.opponent_bench())
    pool = [c for c in hand if is_basic_pokemon(c)]
    if not pool or space <= 0:
        return
    picks = await ctx.choose_cards(pool, min(2, space, len(pool)), minimum=0,
                                   prompt="Put up to 2 Basic Pokémon onto your opponent's Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="d75d49a8-0122-5416-9c4e-627afe70a44e",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic"],
    subtypes=["Basic"],
    collector_number=275,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Attack(
            title="Pulling Currents",
            game_text="Your opponent reveals their hand. Put up to 2 Basic Pokémon you find there onto your opponent's Bench.",
            cost={PokemonTypes.WATER: 1},
            effect=_pulling_currents,
        ),
        Attack(
            title="Aqua Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.snipe_attack(20, also_base=True),
        ),
    ],
)
