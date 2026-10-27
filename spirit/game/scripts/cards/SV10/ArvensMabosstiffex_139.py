"""Arven's Mabosstiff ex (SV10 139 -- JP SV9a 052; English DRI/139, DRI/218, DRI/235). Japanese art.
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


def _undamaged(ctx) -> bool:
    return _own(ctx) == 0


card = PokemonCardDef(
    guid="a27192b2-d515-54ff-9e17-2bd09f56c026",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMabosstiffex.Name",
    display_name="Arven's Mabosstiff ex",
    searchable_by=["Arven's Mabosstiff ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=139,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMaschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Vigorous Tackle",
            game_text="If this Pokémon has no damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_undamaged, 120),
        ),
        Attack(
            title="Boss Headbutt",
            game_text="During your next turn, this Pokémon can't use Boss Headbutt.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)
