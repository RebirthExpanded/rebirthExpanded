"""Furfrou (SM - Forbidden Light 99/131 -- JP SM6 073/094).

Basic Colorless Pokemon. HP 90, weakness Fighting x2, retreat 1.

  Return  [C] 20  You may draw cards until you have 5 cards in your hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


async def return_(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) < 5 and await ctx.ask_yes_no("Draw cards until you have 5 cards in your hand?"):
        await ctx.draw_until(5)


card = PokemonCardDef(
    guid="1fe28347-1d6a-5a8c-a943-5cee3552f505",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furfrou.Name",
    display_name="Furfrou",
    searchable_by=['Furfrou', 'Basic', 'Furfrou'],
    subtypes=['Basic'],
    collector_number=99,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=676,
    abilities=[
        Attack(title="Return", game_text="You may draw cards until you have 5 cards in your hand.",
               cost={PokemonTypes.COLORLESS: 1}, damage=20,
               effect=return_),
    ],
)
