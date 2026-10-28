"""Talonflame (SV2 30 -- JP SV2D 013; English PAL/30). Japanese art.
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


def _hurt(ctx) -> bool:
    return _own(ctx) > 0


card = PokemonCardDef(
    guid="daa8affe-e1a5-5367-99d6-cba762fb6a45",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Fiery Breeze",
            game_text="If this Pokémon has any damage counters on it, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_hurt, 90),
        ),
    ],
)
