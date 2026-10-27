"""Wooloo (SV07 124 -- JP SV7 086; English SCR/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def knock_over(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="4efd8e6d-5346-5c6b-b1ff-add1963934f4",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    display_name="Wooloo",
    searchable_by=["Wooloo", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=831,
    abilities=[
        Attack(
            title="Knock Over",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=knock_over,
        ),
    ],
)
