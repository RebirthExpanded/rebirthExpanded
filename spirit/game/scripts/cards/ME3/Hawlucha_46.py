"""Hawlucha (ME3 46 -- JP M3 045; English POR/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _bench_damaged(ctx) -> bool:
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(ctx.board, p)
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="672cce82-0f1f-578c-9c68-64aac3b495df",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Attack(
            title="Vengeful Kick",
            game_text="If your Benched Pokémon have any damage counters on them, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_bench_damaged, 60),
        ),
    ],
)
