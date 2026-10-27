"""Minior (MF 27 -- JP MF 027; English 30C/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def shoot_meteors(ctx):
    pool = ctx.attached_energies(ctx.attacker)
    if pool:
        await ctx.discard_cards(list(pool))
    await ac.snipe_attack(120, pool="any")(ctx)


card = PokemonCardDef(
    guid="64f8d7d4-7eb8-503b-abe5-779b27b83144",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=774,
    abilities=[
        Attack(
            title="Shoot Meteors",
            game_text="Discard all Energy from this Pokémon, and this attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=shoot_meteors,
        ),
    ],
)
