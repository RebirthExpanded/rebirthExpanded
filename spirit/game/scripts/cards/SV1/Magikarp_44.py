"""Magikarp (SV1 44 -- JP SV1S 013; English SVI/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def jump(ctx):
    results = await ctx.flip_coins(1, "Jump")
    if results and results[0]:
        await ac.snipe_attack(10, pool="any")(ctx)


card = PokemonCardDef(
    guid="cf8a23a5-73d7-59a7-b2fa-481aa2d032b0",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Jump",
            game_text="Flip a coin. If heads, this attack does 10 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=jump,
        ),
    ],
)
