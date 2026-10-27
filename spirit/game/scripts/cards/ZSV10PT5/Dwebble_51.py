"""Dwebble (ZSV10PT5 51 -- JP SV11B 054; English BLK/129, BLK/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0


card = PokemonCardDef(
    guid="f9aed19a-210d-5816-a00b-444699ad5b55",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    display_name="Dwebble",
    searchable_by=["Dwebble", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=557,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.damage_per(_own, 10),
        ),
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
