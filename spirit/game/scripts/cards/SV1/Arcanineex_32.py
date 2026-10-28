"""Arcanine ex (SV1 32 -- JP SV1V 016; English SVI/224, SVI/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="bbd47d56-047b-58f7-aaaa-07f4fbc21b79",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanineex.Name",
    display_name="Arcanine ex",
    searchable_by=["Arcanine ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=32,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Raging Claws",
            game_text="This attack does 10 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(_own, 10, base=30),
        ),
        Attack(
            title="Bright Flame",
            game_text="Discard 2 Fire Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 3},
            damage=250,
            effect=ac.self_energy_discard_attack(count=2, energy_type=_PT.FIRE),
        ),
    ],
)
