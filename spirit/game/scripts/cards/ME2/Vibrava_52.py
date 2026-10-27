"""Vibrava (ME2 52 -- JP M2 046; English PFL/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c72e079e-4986-5c37-acfd-d54011366140",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava",
    searchable_by=["Vibrava", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Super Vibration",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
    ],
)
