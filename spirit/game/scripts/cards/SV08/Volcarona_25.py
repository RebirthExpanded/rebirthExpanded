"""Volcarona (SV08 25 -- JP SV8 014; English SSP/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9fb5f0a4-2f33-576a-a4a8-2dba99a05fda",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Leech Life",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_leech,
        ),
        Attack(
            title="Turbulent Wings",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=ac.recoil_attack(50),
        ),
    ],
)
