"""Alolan Vulpix (SMPJ 147 -- JP SMP 147; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _draw_per_heads_until_tails(ctx):
    """Flip a coin until you get tails. Draw a card for each heads."""
    heads = await ctx.flip_until_tails(ctx.ability.title if ctx.ability else "")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="b61ed2ab-3908-5139-b5a8-7e58d4e80c90",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SMPJ",
    regulation_mark="A",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=0,
    abilities=[
        Attack(
            title="Gather Snow",
            game_text="Flip a coin until you get tails. Draw a card for each heads.",
            cost={PokemonTypes.WATER: 1},
            effect=_draw_per_heads_until_tails,
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
