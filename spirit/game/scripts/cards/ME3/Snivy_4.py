"""Snivy (ME3 4 -- JP M3 004; English POR/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="99f59402-2091-513f-9042-5c16dc2e4137",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy", "Basic"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=495,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
