"""Koraidon ex (SVP 197 -- JP SVM 072; English SVP/197). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _bench_damaged(ctx) -> bool:
    return any(_counters(ctx.board, p) > 0 for p in ctx.my_bench())


card = PokemonCardDef(
    guid="87eebd0c-cf2b-53a9-81fa-3688c195f409",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=197,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Claw Slash",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Revenge Buster",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 120),
        ),
    ],
)
