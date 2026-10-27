"""Piplup (ME2 27 -- JP M2 027; English PFL/27, PFL/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="5f57f924-0863-56d4-a79d-d106fbb0a0ee",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Call for Support",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_supporter_card, count=1, reveal=True, prompt="Choose a Supporter card."),
        ),
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
