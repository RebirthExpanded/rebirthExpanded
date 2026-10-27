"""Great Tusk (SV05 96 -- JP SVHK 010; English TEF/96). Japanese art.
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
    guid="6cccf343-e449-579f-a3f6-83fa625f77c7",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTusk.Name",
    display_name="Great Tusk",
    searchable_by=["Great Tusk", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=96,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Lunge Out",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Wrathful Charge",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 80),
        ),
    ],
)
