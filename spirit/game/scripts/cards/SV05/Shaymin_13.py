"""Shaymin (SV05 13 -- JP SV5K 006; English TEF/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


async def pinpoint_dive(ctx):
    pool = [p for p in ctx.opponent_bench() if _ex_or_v(p)]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Benched Pokémon ex or Pokémon V")
        if target is not None:
            await ctx.deal_damage(60, target=target)


card = PokemonCardDef(
    guid="0e238887-e22d-541c-a860-6bd95529d49d",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Pinpoint Dive",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pokémon ex or Benched Pokémon V. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=pinpoint_dive,
        ),
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
