"""Sprigatito (SV2 13 -- JP SV1a 005; English PAL/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="2267e3b3-b80c-5d6e-9976-cb7ea20eaccc",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    display_name="Sprigatito",
    searchable_by=["Sprigatito", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=906,
    abilities=[
        Attack(
            title="Dig Claws",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
