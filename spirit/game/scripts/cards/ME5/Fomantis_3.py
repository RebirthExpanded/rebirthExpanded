"""Fomantis (ME5 3 -- JP M5 003; English PBL/3, PBL/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="389bb434-482d-59e7-a093-d58e6d07b6c7",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    display_name="Fomantis",
    searchable_by=["Fomantis", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=753,
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
