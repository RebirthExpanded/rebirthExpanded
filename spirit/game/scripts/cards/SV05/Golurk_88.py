"""Golurk (SV05 88 -- JP SV5K 036; English TEF/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


card = PokemonCardDef(
    guid="f5b80f97-ce60-55c7-bee1-7b22f98585aa",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Fighting Fist",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 120),
        ),
    ],
)
