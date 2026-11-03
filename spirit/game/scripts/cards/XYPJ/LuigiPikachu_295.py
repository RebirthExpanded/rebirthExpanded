"""Luigi Pikachu (XYPJ 295 -- JP XYP 295; English Japan only). Japanese art.
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
    guid="aa42d4bd-0120-554c-8a80-8a9afdddf9a8",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuigiPikachu.Name",
    display_name="Luigi Pikachu",
    searchable_by=["Luigi Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=295,
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
            title="Super Dash",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=ac.recoil_attack(20),
        ),
    ],
)
