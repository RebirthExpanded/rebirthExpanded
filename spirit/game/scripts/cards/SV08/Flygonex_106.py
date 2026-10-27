"""Flygon ex (SV08 106 -- JP SV7a 027; English SSP/106, SSP/222). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


async def reversing_storm(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attacker not in ctx.knockouts and await ctx.ask_yes_no("Switch this Pokémon with 1 of your Benched Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch with")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def sonic_peridot(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        if _ex_or_v(p):
            await ctx.deal_damage(100, target=p, ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="2849ac81-a4a4-5c8c-849c-d36640eebd86",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygonex.Name",
    display_name="Flygon ex",
    searchable_by=["Flygon ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=106,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Reversing Storm",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=reversing_storm,
        ),
        Attack(
            title="Sonic Peridot",
            game_text="This attack does 100 damage to each of your opponent's Pokémon ex and Pokémon V. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=sonic_peridot,
        ),
    ],
)
