"""Grubbin (SV05 18 -- JP SV5M 010; English TEF/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _grubbin(card) -> bool:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Grubbin"


card = PokemonCardDef(
    guid="ab74237e-d81e-5cc0-b324-4dc9537b2c96",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    display_name="Grubbin",
    searchable_by=["Grubbin", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=736,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Grubbin and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_bench(_grubbin, count=2, prompt="Choose up to 2 Grubbin."),
        ),
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
