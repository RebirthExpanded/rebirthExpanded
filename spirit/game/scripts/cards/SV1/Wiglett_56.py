"""Wiglett (SV1 56 -- JP SV1S 019; English SVI/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def dig_a_little(ctx):
    results = await ctx.flip_coins(1, "Dig a Little")
    top = list(ctx.deck_top(1, player_id=ctx.opponent_id)) if results and results[0] else []
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="d300d14c-8867-5f77-8bf1-54f405864ee8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Dig a Little",
            game_text="Flip a coin. If heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dig_a_little,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
