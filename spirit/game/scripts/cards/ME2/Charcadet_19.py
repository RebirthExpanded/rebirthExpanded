"""Charcadet (ME2 19 -- JP M2 019; English MEP/22, PFL/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="ef9385f7-36f0-57c9-9e53-45f9ce2ba1ea",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=su.search_to_hand(is_basic_energy_card, count=2, reveal=True, prompt="Choose up to 2 Basic Energy cards."),
        ),
        Attack(
            title="Chop",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
