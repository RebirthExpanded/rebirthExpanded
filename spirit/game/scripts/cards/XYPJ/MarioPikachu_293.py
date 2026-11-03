"""Mario Pikachu (XYPJ 293 -- JP XYP 293; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac



async def _draw_per_heads_until_tails(ctx):
    """Flip a coin until you get tails. Draw a card for each heads."""
    heads = await ctx.flip_until_tails(ctx.ability.title if ctx.ability else "")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="d57d2517-2e49-516e-b2e2-cffd59fd813c",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarioPikachu.Name",
    display_name="Mario Pikachu",
    searchable_by=["Mario Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=293,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Coin Collecting",
            game_text="Flip a coin until you get tails. Draw a card for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_draw_per_heads_until_tails,
        ),
        Attack(
            title="Super Jump",
            game_text="Flip a coin. If heads, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(50),
        ),
    ],
)
