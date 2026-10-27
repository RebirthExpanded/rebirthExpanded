"""Phanpy (ME4 44 -- JP M4 044; English CRI/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e0083581-a6e0-587b-8c7d-7fb4abc0d385",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=231,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
