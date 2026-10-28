"""Meowth (SV035 52 -- JP SV2a 052; English MEW/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def come_here_right_meow(ctx):
    results = await ctx.flip_coins(1, "Come Here Right Meow")
    if results and results[0]:
        await su.gust_attack()(ctx)


card = PokemonCardDef(
    guid="dae7cfac-ce80-50ca-a573-a5dace4824a2",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Come Here Right Meow",
            game_text="Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=come_here_right_meow,
        ),
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
