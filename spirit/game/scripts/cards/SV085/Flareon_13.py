"""Flareon (SV085 13 -- JP SV2a 136; English MEW/136, PRE/13, SVP/167). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _flip_discard_energy(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target) \
            and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


card = PokemonCardDef(
    guid="860f0de1-0124-51f8-8b85-414acc5ec4b9",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Destructive Flame",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=_flip_discard_energy,
        ),
        Attack(
            title="Fighting Blaze",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 90),
        ),
    ],
)
