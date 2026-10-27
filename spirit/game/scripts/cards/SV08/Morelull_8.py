"""Morelull (SV08 8 -- JP SV7a 002; English SSP/8). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c349ca13-cf10-5ec1-bf43-f4910fcb7141",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    display_name="Morelull",
    searchable_by=["Morelull", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=755,
    abilities=[
        Attack(
            title="Attach",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
