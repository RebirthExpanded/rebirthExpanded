"""Remoraid (SV09 33 -- JP SV9 019; English JTG/33). Japanese art.
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
    guid="edb63aee-e8d3-594a-b8e8-4571052d0c2b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Flail",
            game_text="This attack does 10 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=ac.damage_per(_own, 10),
        ),
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
