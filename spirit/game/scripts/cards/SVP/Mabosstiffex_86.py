"""Mabosstiff ex (SVP 86 -- JP SVP 055; English SVP/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _bench_damaged(ctx) -> bool:
    return any(_counters(ctx.board, p) > 0 for p in ctx.my_bench())


card = PokemonCardDef(
    guid="eb4b5c21-0651-54b0-aec1-1ed4f48f6f60",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiffex.Name",
    display_name="Mabosstiff ex",
    searchable_by=["Mabosstiff ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=86,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Daunt",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=pc.debuff_defender_attacks(50),
        ),
        Attack(
            title="Proud Fangs",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 120),
        ),
    ],
)
