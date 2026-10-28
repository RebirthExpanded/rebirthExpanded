"""Tadbulb (SV2 78 -- JP SV2D 024; English PAL/78). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fcc7c190-83e9-5e7f-a05e-6646e87f6c7e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    display_name="Tadbulb",
    searchable_by=["Tadbulb", "Basic"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=938,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
        ),
    ],
)
