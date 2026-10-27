"""Klefki (SV08 128 -- JP SV7a 035; English SSP/128). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def stick_n_draw(ctx):
    if not ctx.hand():
        return
    paid = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")
    if paid:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="ff736d3d-41af-5f86-9b1d-c966df3b4659",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=707,
    abilities=[
        Attack(
            title="Stick 'n' Draw",
            game_text="Discard a card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=stick_n_draw,
        ),
        Attack(
            title="Hook",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
