"""Purrloin (SV4 114 -- JP SV4K 047; English PAR/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="6f6763cf-585b-56ed-a92c-bacbed010d40",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Cat Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
