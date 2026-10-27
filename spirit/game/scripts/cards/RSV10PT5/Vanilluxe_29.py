"""Vanilluxe (RSV10PT5 29 -- JP SV11W 026; English WHT/113, WHT/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def double_freeze(ctx):
    heads = sum(1 for r in await ctx.flip_coins(2, "Double Freeze") if r)
    if heads:
        await ctx.deal_damage(90 * heads)
        target = ctx.opponent_active()
        if target is not None and target not in ctx.knockouts:
            await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="4aec33d8-6ac0-5339-9242-2de322bdca32",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Double Freeze",
            game_text="Flip 2 coins. This attack does 90 damage for each heads. If either of them is heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="x",
            effect=double_freeze,
        ),
    ],
)
