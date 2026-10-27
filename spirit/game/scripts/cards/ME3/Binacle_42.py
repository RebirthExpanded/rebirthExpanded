"""Binacle (ME3 42 -- JP M3 041; English MEP/87, POR/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="132d57df-db50-55e0-887d-2648a987b43f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    display_name="Binacle",
    searchable_by=["Binacle", "Basic"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=688,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
