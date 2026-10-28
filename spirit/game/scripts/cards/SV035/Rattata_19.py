"""Rattata (SV035 19 -- JP SV2a 019; English MEW/19). Japanese art.
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
    guid="8b98cd60-113f-5b12-9e74-5ca3f63625da",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Attack(
            title="Gnaw the Wound",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.damage_per(_defender_counters, 10, base=20),
        ),
    ],
)
