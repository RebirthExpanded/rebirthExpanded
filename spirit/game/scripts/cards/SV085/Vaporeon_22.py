"""Vaporeon (SV085 22 -- JP SV2a 134; English MEW/134, PRE/22, SVP/168). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


card = PokemonCardDef(
    guid="942e744f-86df-5424-8ca0-5abff4720551",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Spiral Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Fighting Whirlpool",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 90),
        ),
    ],
)
