"""Audino (ZSV10PT5 74 -- JP SV11B 076; English BLK/151, BLK/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def return_(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="20c48820-4d99-57dd-afe6-e075eb0ab33d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Return",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=return_,
        ),
    ],
)
