"""Drifloon (SV1 89 -- JP SV1S 029; English PAF/155, SVI/89). Japanese art.
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
    guid="df962c85-550f-5fed-824b-96bcd295a303",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title="Gust",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
        Attack(
            title="Balloon Blast",
            game_text="This attack does 30 damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(_own, 30),
        ),
    ],
)
