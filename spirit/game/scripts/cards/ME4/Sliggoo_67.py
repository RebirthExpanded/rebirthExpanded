"""Sliggoo (ME4 67 -- JP M4 065; English CRI/67, CRI/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0a09d55c-aa79-58f1-a962-14d03bcbb278",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    display_name="Sliggoo",
    searchable_by=["Sliggoo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goomy.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=70,
        ),
    ],
)
