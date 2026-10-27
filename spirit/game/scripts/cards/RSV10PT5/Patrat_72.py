"""Patrat (RSV10PT5 72 -- JP SV11W 070; English WHT/152, WHT/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="747dd833-54b0-5aa4-8ba8-90ff4d4be9f9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat", "Basic"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Attack(
            title="Procurement",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."),
        ),
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
