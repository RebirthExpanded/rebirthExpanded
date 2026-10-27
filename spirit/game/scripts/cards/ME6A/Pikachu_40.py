"""Pikachu (ME6A 40 -- JP M6a 040; English 30C/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def get_some_air(ctx):
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="63afce63-f170-54d9-958f-dc529c84e3ed",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Get Some Air",
            game_text="This Pokémon recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=get_some_air,
        ),
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
