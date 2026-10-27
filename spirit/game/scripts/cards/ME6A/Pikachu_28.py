"""Pikachu (ME6A 28 -- JP M6a 028; English 30C/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _pikachus(pokemon) -> bool:
    return getattr(def_for(pokemon.archetype_id), "display_name", None) in ("Pikachu", "Pikachu ex")


card = PokemonCardDef(
    guid="46577e64-59fc-518a-9738-e5861a596bf4",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Chain",
            game_text="This attack does 40 damage for each of your Pikachu and Pikachu ex in play.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine", pred=_pikachus), 40),
        ),
    ],
)
