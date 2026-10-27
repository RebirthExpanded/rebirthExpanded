"""Meditite (ME2PT5 103 -- JP M2a 084; English ASC/103). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="ae7a0f4c-b667-55d7-b700-7bbe7f6d2c6a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    display_name="Meditite",
    searchable_by=["Meditite", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=307,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(1),
        ),
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
