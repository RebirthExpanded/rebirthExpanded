"""Trevenant (SV06 13 -- JP SV6 007; English TWM/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)


card = PokemonCardDef(
    guid="ca6ce591-1f44-5029-9c26-2c0a5775c2bd",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_leech,
        ),
        Attack(
            title="Forest Dump",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
