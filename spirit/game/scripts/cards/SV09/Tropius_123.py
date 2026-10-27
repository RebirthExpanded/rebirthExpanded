"""Tropius (SV09 123 -- JP SVM 101; English JTG/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def fruit_bearing(ctx):
    if not ctx.hand():
        return
    paid = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card from your hand")
    if paid:
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="b524c380-f73c-5941-8a7d-87c6b187e3bf",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=357,
    abilities=[
        Attack(
            title="Fruit Bearing",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=fruit_bearing,
        ),
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
