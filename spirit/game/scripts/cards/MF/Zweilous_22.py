"""Zweilous (MF 22 -- JP MF 022; English 30C/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4b3ff71c-ebf9-50b4-9c6d-9eb8e5b3db6d",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
