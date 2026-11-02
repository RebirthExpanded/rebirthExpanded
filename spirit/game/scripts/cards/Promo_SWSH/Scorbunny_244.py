"""Scorbunny (Promo_SWSH 244 -- JP SP 255; English SP/244). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _flaring_dash(ctx):
    heads = await ctx.flip_until_tails("Flaring Dash")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="37d106da-c5b4-549b-9815-95f5fdb4bb18",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic"],
    subtypes=["Basic"],
    collector_number=244,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Flaring Dash",
            game_text="Flip a coin until you get tails. For each heads, draw a card.",
            cost={PokemonTypes.FIRE: 1},
            effect=_flaring_dash,
        ),
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
