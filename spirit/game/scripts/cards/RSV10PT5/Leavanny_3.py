"""Leavanny (RSV10PT5 3 -- JP SV11W 003; English WHT/3, WHT/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon_in_play


async def healing_wrapping(ctx):
    for p in ctx.my_pokemon_in_play():
        if is_basic_pokemon_in_play(p):
            await ctx.heal(100, p)


card = PokemonCardDef(
    guid="c64c1593-bc01-5589-85e7-3b47717eadb7",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Healing Wrapping",
            game_text="Heal 100 damage from each of your Basic Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=healing_wrapping,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.flip_bonus(40),
        ),
    ],
)
