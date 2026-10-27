"""Servine (ME3 5 -- JP M3 005; English POR/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="8868b46b-7d87-5205-bf11-ce6610a89c3f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    display_name="Servine",
    searchable_by=["Servine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Solar Cutter",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)
