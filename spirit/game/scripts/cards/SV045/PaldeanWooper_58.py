"""Paldean Wooper (SV045 58 -- JP SV1a 053; English PAF/180, PAF/58, PAL/128, PAL/221). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_stadium_card


card = PokemonCardDef(
    guid="59aec80a-237d-5934-9fe7-6dd7d94089f3",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    display_name="Paldean Wooper",
    searchable_by=["Paldean Wooper", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=194,
    abilities=[
        Attack(
            title="Find a Home",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.search_to_hand(is_stadium_card, count=1, reveal=True, prompt="Choose a Stadium card."),
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
