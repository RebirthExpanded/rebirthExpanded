"""Xerneas (ME6A 63 -- JP M6a 063; English 30C/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_stadium_card


card = PokemonCardDef(
    guid="5bd0ea41-8f60-57ca-9cef-1d939fa038d3",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geonavigation",
            game_text="Search your deck for up to 2 Stadium card, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_stadium_card, count=2, reveal=True, prompt="Choose up to 2 Stadium cards."),
        ),
        Attack(
            title="Aurora Horns",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
