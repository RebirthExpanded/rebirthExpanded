"""Wattrel (SV2 81 -- JP SV1a 032; English PAL/81). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def devastating_wind(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if hand:
        await ctx.shuffle_into_deck(hand, ctx.opponent_id)
    else:
        await ctx.shuffle_deck(ctx.opponent_id)
    await ctx.draw_cards(4, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="0c9466af-e6f9-5831-9f18-3cfdd7c1b9a0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    display_name="Wattrel",
    searchable_by=["Wattrel", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=940,
    abilities=[
        Attack(
            title="Devastating Wind",
            game_text="Your opponent shuffles their hand into their deck and draws 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=devastating_wind,
        ),
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
