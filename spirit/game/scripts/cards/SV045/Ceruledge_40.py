"""Ceruledge (SV045 40 -- JP SV2D 031; English PAF/162, PAF/40, PAL/98). Japanese art.
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
    guid="77d9b745-d75c-5e9b-8b46-d289b29bebdd",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Life Sucker",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Fighting Sword",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 100),
        ),
    ],
)
