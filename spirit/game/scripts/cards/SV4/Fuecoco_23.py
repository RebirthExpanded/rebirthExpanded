"""Fuecoco (SV4 23 -- JP SVEL 005; English PAR/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="927ee409-6483-5e7d-8ff7-23c515222e6f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
