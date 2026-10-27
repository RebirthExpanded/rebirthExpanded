"""Clauncher (ME1 37 -- JP M1S 019; English MEG/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="da0b5a12-30ba-572e-8a33-23efd5c79b5c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    display_name="Clauncher",
    searchable_by=["Clauncher", "Basic"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=692,
    abilities=[
        Attack(
            title="Wave Splash",
            game_text="",
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)
