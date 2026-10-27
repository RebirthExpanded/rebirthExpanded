"""Cosmog (ME6A 64 -- JP M6a 064; English 30C/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="abe82a18-44ee-5a16-aa1e-6a1adb3114f2",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    display_name="Cosmog",
    searchable_by=["Cosmog", "Basic"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=789,
    abilities=[
        Attack(
            title="Splash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
