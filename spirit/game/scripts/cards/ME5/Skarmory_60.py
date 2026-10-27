"""Skarmory (ME5 60 -- JP M5 058; English PBL/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_metal(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.METAL)


card = PokemonCardDef(
    guid="c63721a5-116d-5523-b120-e446642fa612",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=227,
    abilities=[
        Attack(
            title="Steel Cutter",
            game_text="Discard up to 2 Basic Metal Energy cards from your hand, and this attack does 40 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 1},
            damage=40,
            damage_operator="x",
            effect=ac.discard_for_bonus("hand", predicate=_basic_metal, max_count=2, per=40, base=0, prompt="Discard up to 2 Basic Metal Energy cards from your hand."),
        ),
    ],
)
