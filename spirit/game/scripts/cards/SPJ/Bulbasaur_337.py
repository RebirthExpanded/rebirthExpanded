"""Bulbasaur (SPJ 337 -- JP SP 337; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _gather_and_swing(ctx):
    heads = await ctx.flip_until_tails("Gather and Swing")
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="706ab0bb-290f-56d1-8c03-7687ac7ad109",
    key="SPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic"],
    subtypes=["Basic"],
    collector_number=337,
    set_code="SPJ",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Gather and Swing",
            game_text="Flip a coin until you get tails. For each heads, draw a card.",
            cost={PokemonTypes.GRASS: 1},
            effect=_gather_and_swing,
        ),
    ],
)
