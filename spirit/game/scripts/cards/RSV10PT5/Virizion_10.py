"""Virizion (RSV10PT5 10 -- JP SV11W 010; English WHT/10, WHT/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _leech(ctx):
    dealt = await ctx.deal_damage()
    if dealt:
        await ctx.heal(dealt, ctx.attacker)
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="11f9b9ba-c6cd-51ff-b344-010979a2bcbe",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=_leech,
        ),
        Attack(
            title="Emerald Blade",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=_hit_then_lock,
        ),
    ],
)
