"""Remoraid (ME4 16 -- JP M4 016; English CRI/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="61e5d03b-8419-5ebc-8c8a-919f7e86756f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
