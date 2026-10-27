"""Glalie (SV06 52 -- JP SV6 032; English TWM/52). Japanese art.
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
    guid="7074fe82-88c4-59b9-af2b-8d33cf1d7a6c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Damage Beat",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_defender_counters, 20),
        ),
        Attack(
            title="Crazy Headbutt",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
