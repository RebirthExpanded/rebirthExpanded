"""Ferroseed (SV4 127 -- JP SV3a 043; English PAR/127). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="cfe1a9bf-2a86-535a-8b89-dc3a6f4d7fae",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=597,
    abilities=[
        Attack(
            title="Spike Sting",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
