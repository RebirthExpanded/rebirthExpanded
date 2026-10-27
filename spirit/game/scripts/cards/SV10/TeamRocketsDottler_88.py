"""Team Rocket's Dottler (SV10 88 -- JP SV10 043; English DRI/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def disruptive_radar(ctx):
    await ctx.reorder_deck_top(5, player_id=ctx.opponent_id,
                               prompt="Rearrange the top cards of your opponent's deck")


card = PokemonCardDef(
    guid="9f5d8970-8808-5ff9-b435-cb1fe11fafe7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDottler.Name",
    display_name="Team Rocket's Dottler",
    searchable_by=["Team Rocket's Dottler", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsBlipbug.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Disruptive Radar",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=disruptive_radar,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
