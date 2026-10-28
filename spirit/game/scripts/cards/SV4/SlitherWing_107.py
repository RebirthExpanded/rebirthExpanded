"""Slither Wing (SV4 107 -- JP SV4K 041; English PAR/107, PAR/203). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def burning_turbulence(ctx):
    await ctx.deal_damage()
    await ctx.deal_damage(90, target=ctx.attacker, apply_modifiers=False)
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts:
        await ctx.apply_special_condition(d, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="232872bf-3d6f-58ca-8c3a-0741bf0c0f5b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlitherWing.Name",
    display_name="Slither Wing",
    searchable_by=["Slither Wing", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=107,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=988,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=ac.mill_attack(1),
        ),
        Attack(
            title="Burning Turbulence",
            game_text="This Pokémon also does 90 damage to itself. Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=120,
            effect=burning_turbulence,
        ),
    ],
)
