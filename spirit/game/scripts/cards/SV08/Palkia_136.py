"""Palkia (SV08 136 -- JP SV7a 043; English SSP/136). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card


async def space_crash(ctx):
    n = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_basic_energy_card(e))
    if n:
        await ctx.deal_damage(40 * n)


card = PokemonCardDef(
    guid="7eb63f05-ba21-5f04-95f2-f62fcfc2e284",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name",
    display_name="Palkia",
    searchable_by=["Palkia", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=484,
    abilities=[
        Attack(
            title="Space Crash",
            game_text="This attack does 40 damage for each Basic Energy attached to this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=space_crash,
        ),
    ],
)
