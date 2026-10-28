"""Lokix (SV4 122 -- JP SV4K 052; English PAR/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
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
    guid="5a0f1c1c-e9d5-5696-8a3d-e4e65bcb98e9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lokix.Name",
    display_name="Lokix",
    searchable_by=["Lokix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name",
    family_id=919,
    abilities=[
        Attack(
            title="Bounce",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=su.switch_self_attack(),
        ),
        Attack(
            title="Punishing Kick",
            game_text="This attack does 40 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=ac.damage_per(_defender_counters, 40, base=10),
        ),
    ],
)
