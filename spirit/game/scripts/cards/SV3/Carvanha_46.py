"""Carvanha (SV3 46 -- JP SV3 021; English OBF/46, SVP/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3f356514-f1ff-5ba2-92ce-620c4fbd0574",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
