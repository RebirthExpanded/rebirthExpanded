"""Stunky (ME4 53 -- JP M4 052; English CRI/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="dc3ccb8c-16ab-55d7-841a-190f6d2ee890",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    display_name="Stunky",
    searchable_by=["Stunky", "Basic"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=434,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
