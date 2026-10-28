"""Remoraid (SV4 33 -- JP SV3a 003; English PAR/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="d5d0d0a8-d0c7-5c1a-85d3-fca37fa3ddde",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Sprinkle Water",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
