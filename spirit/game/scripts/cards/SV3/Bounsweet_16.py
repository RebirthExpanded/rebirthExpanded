"""Bounsweet (SV3 16 -- JP SV2P 007; English OBF/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f1514af5-6398-538f-b3b8-fd1c1a982322",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    display_name="Bounsweet",
    searchable_by=["Bounsweet", "Basic"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=761,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=ac.recoil_attack(10),
        ),
    ],
)
