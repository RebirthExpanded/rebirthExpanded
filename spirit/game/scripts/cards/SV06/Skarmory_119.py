"""Skarmory (SV06 119 -- JP SV6 072; English TWM/119). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _discard_any_stadium(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


async def big_storm(ctx):
    await ctx.deal_damage()
    await _discard_any_stadium(ctx)


card = PokemonCardDef(
    guid="2e74c767-98f8-59dc-9e2a-c993b65f0af8",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=227,
    abilities=[
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
        Attack(
            title="Big Storm",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=big_storm,
        ),
    ],
)
