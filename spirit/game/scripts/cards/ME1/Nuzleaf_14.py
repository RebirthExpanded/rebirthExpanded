"""Nuzleaf (ME1 14 -- JP M1L 008; English MEG/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7c639824-fa45-5ace-83de-7e9048527e1e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Pound",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
