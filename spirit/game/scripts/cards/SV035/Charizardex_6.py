"""Charizard ex (SV035 6 -- JP SV2a 006; English MEW/183, MEW/199, MEW/6, SVP/161). Japanese art.
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
    guid="759496a2-0f4f-5969-88d5-5b5c6b827d63",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name",
    display_name="Charizard ex",
    searchable_by=["Charizard ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=6,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Brave Wing",
            game_text="If this Pokémon has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_hurt, 100),
        ),
        Attack(
            title="Explosive Vortex",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 4},
            damage=330,
            effect=ac.self_energy_discard_attack(count=3),
        ),
    ],
)
