"""Poké-Tele AD Pikachu (XYPJ 56 -- JP XYP 056; English Japan only). Japanese art.
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
    guid="3c50805f-2e73-52e0-8b08-673d8ee3e952",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PokeTeleADPikachu.Name",
    display_name="Poké-Tele AD Pikachu",
    searchable_by=["Poké-Tele AD Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Poké-Tele Challenge",
            game_text="Flip a coin until you get tails. Draw a card for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_draw_per_heads_until_tails,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
