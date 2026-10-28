"""Rellor (SV2 25 -- JP SV2P 013; English PAL/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3bbcc892-d4b3-53aa-87bd-abde6f131fcf",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    display_name="Rellor",
    searchable_by=["Rellor", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=953,
    abilities=[
        Attack(
            title="Bug Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
