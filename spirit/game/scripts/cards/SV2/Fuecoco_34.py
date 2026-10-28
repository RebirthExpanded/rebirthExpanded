"""Fuecoco (SV2 34 -- JP SV1a 017; English PAL/34, SVP/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2be388b2-33d9-5e71-9f0d-ae895f1ef686",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV2",
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
            title="Tackle",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
