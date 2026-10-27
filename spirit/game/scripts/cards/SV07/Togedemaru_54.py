"""Togedemaru (SV07 54 -- JP SV7 036; English SCR/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def electrifying_chance(ctx):
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if ac.count_prizes_remaining("mine")(ctx) == 1 and target is not None and target not in ctx.knockouts:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="6d4f205f-5799-5220-8912-6e3b446a3791",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=777,
    abilities=[
        Attack(
            title="Electrifying Chance",
            game_text="If you have exactly 1 Prize card remaining, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=electrifying_chance,
        ),
    ],
)
