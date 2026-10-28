"""Maschiff (SV2 142 -- JP SV2P 048; English PAL/142). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="baf67643-0965-56f7-89a5-3cdb7d6528a0",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    display_name="Maschiff",
    searchable_by=["Maschiff", "Basic"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
