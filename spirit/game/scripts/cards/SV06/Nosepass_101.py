"""Nosepass (SV06 101 -- JP SV5a 043; English TWM/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def power_rush(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Power Rush")
    if results and not results[0]:
        ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="92d0d3e1-87fa-52a1-8906-462d2513c279",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=299,
    abilities=[
        Attack(
            title="Power Rush",
            game_text="Flip a coin. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=power_rush,
        ),
    ],
)
