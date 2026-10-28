"""Rowlet (SV3 13 -- JP SVD 006; English OBF/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6b96f98e-81af-5ed8-8b2d-0311bedd0552",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
