"""Popplio (ME5 18 -- JP M5 017; English PBL/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e964be7d-43bc-5f15-adea-b172bce838d7",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    display_name="Popplio",
    searchable_by=["Popplio", "Basic"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=728,
    abilities=[
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
