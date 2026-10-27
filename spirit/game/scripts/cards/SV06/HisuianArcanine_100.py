"""Hisuian Arcanine (SV06 100 -- JP SV5a 042; English TWM/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _bench_damaged(ctx) -> bool:
    return any(_counters(ctx.board, p) > 0 for p in ctx.my_bench())


card = PokemonCardDef(
    guid="928f61c2-b1d4-5c30-b5e4-375c10be4674",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianArcanine.Name",
    display_name="Hisuian Arcanine",
    searchable_by=["Hisuian Arcanine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Proud Fangs",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 90 more damage.",
            cost={},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 90),
        ),
        Attack(
            title="Searing Flame",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
