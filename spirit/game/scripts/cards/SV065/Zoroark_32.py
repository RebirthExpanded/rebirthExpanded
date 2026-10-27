"""Zoroark (SV065 32 -- JP SV6a 032; English SFA/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


def _opp_ex_v(ctx) -> int:
    return sum(1 for p in ctx.opponent_pokemon_in_play() if _ex_or_v(p))


card = PokemonCardDef(
    guid="10a45aa7-311e-5e49-9316-a0fd36f3f3e9",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Illusory Hijacking",
            game_text="This attack does 60 damage for each of your opponent's Pokémon ex and Pokémon V in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=ac.damage_per(_opp_ex_v, 60),
        ),
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)
