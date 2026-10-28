"""Glimmet (SV2 125 -- JP SV2P 043; English PAL/125). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="ad51d5aa-daf8-5e5c-bb22-93af805a86e1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Rock Throw",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
