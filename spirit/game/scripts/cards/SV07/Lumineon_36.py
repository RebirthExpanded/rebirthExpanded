"""Lumineon (SV07 36 -- JP SV7 021; English SCR/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _maybe_draw_to_6(ctx):
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


async def return_(ctx):
    await ctx.deal_damage()
    await _maybe_draw_to_6(ctx)


card = PokemonCardDef(
    guid="899fd652-ba71-598d-ad52-f5b9cb8a745b",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lumineon.Name",
    display_name="Lumineon",
    searchable_by=["Lumineon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    family_id=456,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=return_,
        ),
        Attack(
            title="Razor Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
