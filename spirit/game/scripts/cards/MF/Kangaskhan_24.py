"""Kangaskhan (MF 24 -- JP MF 024; English 30C/114). Japanese art.
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


card = PokemonCardDef(
    guid="e0c521cc-b0c6-5494-994c-c626e2393d28",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name",
    display_name="Kangaskhan",
    searchable_by=["Kangaskhan", "Basic"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Rage",
            game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(_own, 10, base=20),
        ),
        Attack(
            title="Mega Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
