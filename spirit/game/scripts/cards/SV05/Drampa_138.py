"""Drampa (SV05 138 -- JP SV5M 060; English TEF/138, TEF/184). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _all_bench_damaged(ctx) -> bool:
    bench = ctx.my_bench()
    return bool(bench) and all(_counters(ctx.board, p) > 0 for p in bench)


card = PokemonCardDef(
    guid="59ede4a1-3ef8-5e59-89ba-49657ce9d680",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=780,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Raging Cannon",
            game_text="If all of your Benched Pokémon have at least 1 damage counter on them, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_all_bench_damaged, 120),
        ),
    ],
)
