"""Feebas (SV4 35 -- JP SV4M 013; English PAR/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_energy_card


card = PokemonCardDef(
    guid="5f1013b7-3b0a-5a38-8f3f-18cee3823f8a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Drawup Power",
            game_text="Search your deck for an Energy card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=su.search_to_hand(is_energy_card, count=1, reveal=True, prompt="Choose an Energy card."),
        ),
    ],
)
