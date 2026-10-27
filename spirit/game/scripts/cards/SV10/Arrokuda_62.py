"""Arrokuda (SV10 62 -- JP SV10 029; English DRI/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8ac1585a-a9cd-5977-8a6c-8fb60c4788f5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
