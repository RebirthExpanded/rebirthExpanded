"""Dress-Up Pikachu (XYPJ 99 -- JP XYP 099; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac



async def _synchro_appeal(ctx):
    n = len(ctx.my_bench())
    if not n:
        return
    results = await ctx.flip_coins(n, ctx.ability.title if ctx.ability else "")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="1d5edc08-a389-5c3f-abd6-a766281ae7c1",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DressUpPikachu.Name",
    display_name="Dress-Up Pikachu",
    searchable_by=["Dress-Up Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(10),
        ),
        Attack(
            title="Synchro Appeal",
            game_text="Flip a coin for each of your Benched Pokémon. Draw a card for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=_synchro_appeal,
        ),
    ],
)
