"""Zorua (MF 19 -- JP MF 019; English 30C/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7223f279-7312-52fe-8111-87c66246683d",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=570,
    abilities=[
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
        ),
    ],
)
