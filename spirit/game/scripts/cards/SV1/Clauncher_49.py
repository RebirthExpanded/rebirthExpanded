"""Clauncher (SV1 49 -- JP SV1V 021; English SVI/205, SVI/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e3ba8716-c676-5c04-96f9-20c476bf60a9",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    display_name="Clauncher",
    searchable_by=["Clauncher", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=692,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
