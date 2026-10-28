"""Meltan (SV3 152 -- JP SVD 084; English OBF/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="77f6aa01-fa58-5a9d-90b6-e1bd463ad6c4",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=808,
    abilities=[
        Attack(
            title="Melt",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
