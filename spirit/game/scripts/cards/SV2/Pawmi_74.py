"""Pawmi (SV2 74 -- JP SVC 007; English PAL/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="20d448fb-5e00-5e24-9cf9-870c2ae50ee6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    display_name="Pawmi",
    searchable_by=["Pawmi", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=921,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
