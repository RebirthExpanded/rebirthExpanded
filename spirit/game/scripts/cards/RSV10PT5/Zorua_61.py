"""Zorua (RSV10PT5 61 -- JP SV11W 058; English WHT/142, WHT/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="3d0ab90e-7c9a-5cac-a11c-9b04c6e57057",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=570,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
