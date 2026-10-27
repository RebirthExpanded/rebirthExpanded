"""Snorlax (SV08 144 -- JP SVLN 010; English SSP/144). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def spike_draw(ctx):
    await ctx.deal_damage()
    await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="2d8fe53a-a187-5936-adfe-429f3ecee453",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=spike_draw,
        ),
        Attack(
            title="Mega Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
