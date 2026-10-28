"""Wiglett (SV3 58 -- JP SVD 030; English OBF/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fb375179-85b5-5e28-ab14-6db28f22a525",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    display_name="Wiglett",
    searchable_by=["Wiglett", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV3",
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
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
