"""Squawkabilly (SV1 162 -- JP SV1V 067; English SVI/162). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import passives_common as pc


async def fly(ctx):
    results = await ctx.flip_coins(1, "Fly")
    if not (results and results[0]):
        return
    await ctx.deal_damage()
    await pc.apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="e759dbf4-2cb0-5d21-809a-b3855eef2486",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name",
    display_name="Squawkabilly",
    searchable_by=["Squawkabilly", "Basic"],
    subtypes=["Basic"],
    collector_number=162,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=931,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(count=2, prompt="Choose up to 2 Basic Pokémon to put onto your Bench."),
        ),
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=fly,
        ),
    ],
)
