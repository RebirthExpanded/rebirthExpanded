"""Wiglett (SV4 52 -- JP SV4K 024; English PAR/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="0e565970-ea7c-5468-a60e-9cf690d29a62",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=960,
    abilities=[
        Attack(
            title="Vibration",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
