"""Swoobat (SV045 33 -- JP SV4K 029; English PAF/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions


async def attraction_wave(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.CONFUSED, confusion_counters=6)


card = PokemonCardDef(
    guid="60abeb66-4b10-5ecc-b6c1-0cc212fda437",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Attraction Wave",
            game_text="Your opponent's Active Pokémon is now Confused. Put 6 damage counters instead of 3 on that Pokémon for this Special Condition.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=attraction_wave,
        ),
    ],
)
