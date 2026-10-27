"""Litleo (ME4 14 -- JP M4 014; English CRI/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3d8dd2f9-0c48-540a-8fcf-146037c80913",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    display_name="Litleo",
    searchable_by=["Litleo", "Basic"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=667,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
