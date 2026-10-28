"""Bonsly (SV3 110 -- JP SV3 058; English OBF/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9d102be1-9279-5fdf-bb35-4a273f031899",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bonsly.Name",
    display_name="Bonsly",
    searchable_by=["Bonsly", "Basic"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    family_id=438,
    abilities=[
        Attack(
            title="Blubbering",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
