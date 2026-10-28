"""Wimpod (SV4 48 -- JP SV4K 021; English PAR/191, PAR/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def sneaky_snacking(ctx):
    results = await ctx.flip_coins(1, "Sneaky Snacking")
    if results and results[0]:
        await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="ffb85113-f8cb-5c3f-ba98-c87bc4e865ef",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Attack(
            title="Sneaky Snacking",
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sneaky_snacking,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
