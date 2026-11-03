"""Vulpix (SMPJ 146 -- JP SMP 146; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _draw_per_heads_until_tails(ctx):
    """Flip a coin until you get tails. Draw a card for each heads."""
    heads = await ctx.flip_until_tails(ctx.ability.title if ctx.ability else "")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="1530baa4-a24a-5795-a3b7-e38f2d8eaaac",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SMPJ",
    regulation_mark="A",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Collect Fallen Leaves",
            game_text="Flip a coin until you get tails. Draw a card for each heads.",
            cost={PokemonTypes.FIRE: 1},
            effect=_draw_per_heads_until_tails,
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
