"""Clefairy (SV035 35 -- JP SV2a 035; English MEW/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _clefairy(card) -> bool:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Clefairy"


card = PokemonCardDef(
    guid="12518477-4715-5581-a731-0c1acd18d90b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=173,
    abilities=[
        Attack(
            title="Moon-Viewing Invitation",
            game_text="Search your deck for up to 3 Clefairy and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=su.search_to_bench(_clefairy, count=3, prompt="Choose up to 3 Clefairy."),
        ),
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
