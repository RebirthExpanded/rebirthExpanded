"""Tarountula (SV1 16 -- JP SVAM 007; English SVI/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


async def string_haul(ctx):
    results = await ctx.flip_coins(1, "String Haul")
    if results and results[0]:
        await su.gust_attack()(ctx)


card = PokemonCardDef(
    guid="6d5cc46a-6b5e-58ca-8408-79ba229b85e4",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name",
    display_name="Tarountula",
    searchable_by=["Tarountula", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=917,
    abilities=[
        Attack(
            title="String Haul",
            game_text="Flip a coin. If heads, switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=string_haul,
        ),
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
