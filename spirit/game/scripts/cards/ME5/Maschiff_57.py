"""Maschiff (ME5 57 -- JP M5 055; English PBL/57). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c0827730-4de7-5203-9847-0bcbf90de665",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    display_name="Maschiff",
    searchable_by=["Maschiff", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
        ),
    ],
)
