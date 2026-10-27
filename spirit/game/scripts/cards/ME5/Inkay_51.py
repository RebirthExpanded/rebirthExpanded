"""Inkay (ME5 51 -- JP M5 049; English PBL/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="0a86e70b-4140-56d2-bdaa-d6eb1a09e3b3",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Procurement",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."),
        ),
        Attack(
            title="Spinning Attack",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)
