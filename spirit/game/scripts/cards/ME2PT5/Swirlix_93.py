"""Swirlix (ME2PT5 93 -- JP MC 333; English ASC/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="a4062224-ebf7-5997-8a74-206b1ceee27f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=684,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
