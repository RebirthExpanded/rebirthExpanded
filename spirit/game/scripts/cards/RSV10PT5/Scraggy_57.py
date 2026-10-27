"""Scraggy (RSV10PT5 57 -- JP SV11W 054; English WHT/138, WHT/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e8f08fc1-6ee2-5916-872d-4c98c5d3dbd9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    display_name="Scraggy",
    searchable_by=["Scraggy", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Invade",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)
