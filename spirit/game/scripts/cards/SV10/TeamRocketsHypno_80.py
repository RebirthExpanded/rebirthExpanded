"""Team Rocket's Hypno (SV10 80 -- JP SV10 038; English DRI/80). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def bench_manipulation(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    results = await ctx.flip_coins(len(bench), "Bench Manipulation", flipper_id=ctx.opponent_id)
    tails = sum(1 for r in results if not r)
    if tails:
        await ctx.deal_damage(80 * tails, ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="a556ce63-ebd5-5c7b-8ffb-0dd79da90f09",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHypno.Name",
    display_name="Team Rocket's Hypno",
    searchable_by=["Team Rocket's Hypno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=80,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDrowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Psyshot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
        Attack(
            title="Bench Manipulation",
            game_text="Your opponent flips a coin for each of their Benched Pokémon. This attack does 80 damage to your opponent's Active Pokémon for each tails. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=80,
            damage_operator="x",
            effect=bench_manipulation,
        ),
    ],
)
