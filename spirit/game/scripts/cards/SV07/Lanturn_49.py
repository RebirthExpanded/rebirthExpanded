"""Lanturn (SV07 49 -- JP SV7 031; English SCR/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)


async def disorienting_flash(ctx):
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED, confusion_counters=8)


card = PokemonCardDef(
    guid="b92b4db7-abff-5fdd-86aa-5bb44e78547a",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name",
    display_name="Lanturn",
    searchable_by=["Lanturn", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    family_id=170,
    abilities=[
        Attack(
            title="Disorienting Flash",
            game_text="Your opponent's Active Pokémon is now Confused. Put 8 damage counters instead of 3 on that Pokémon for this Special Condition.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=disorienting_flash,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=_hit_then_lock,
        ),
    ],
)
