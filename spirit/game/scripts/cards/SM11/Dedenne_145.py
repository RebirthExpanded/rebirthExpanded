"""Dedenne (SM - Unified Minds 145/236 -- JP SM11 064/094).

Basic Fairy Pokemon. HP 70, weakness Metal x2, resistance Darkness -20,
retreat 1.

  Return  [C] 20  You may draw cards until you have 6 cards in your hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


async def return_(ctx):
    await ctx.deal_damage()
    hand = ctx.hand()
    if len(hand) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="b81325ed-704e-5444-983b-a8c5b5f028bc",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=['Dedenne', 'Basic', 'Dedenne'],
    subtypes=['Basic'],
    collector_number=145,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(title="Return", game_text="You may draw cards until you have 6 cards in your hand.",
               cost={PokemonTypes.COLORLESS: 1}, damage=20,
               effect=return_),
    ],
)
