"""Charjabug (SV07 52 -- JP SV7 034; English SCR/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _charjabug(card) -> bool:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Charjabug"


card = PokemonCardDef(
    guid="aee35c40-1fb5-5f46-92a7-3c393904e3c5",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    display_name="Charjabug",
    searchable_by=["Charjabug", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Parallel Placement",
            game_text="Search your deck for up to 3 Charjabug and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=su.search_to_bench(_charjabug, count=3, prompt="Choose up to 3 Charjabug."),
        ),
    ],
)
