"""Detective Pikachu (SVPJ 98 -- JP SVP 098; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def accurate_surveying(ctx):
    heads = await ctx.flip_until_tails("Accurate Surveying")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="2e5db03a-912f-568b-b40f-c708aa200b7f",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DetectivePikachu.Name",
    display_name="Detective Pikachu",
    searchable_by=["Detective Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SVPJ",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=0,
    abilities=[
        Attack(
            title="Accurate Surveying",
            game_text="Flip a coin until you get tails. For each heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=accurate_surveying,
        ),
        Attack(
            title="Ride Dash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
