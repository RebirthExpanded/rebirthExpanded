"""Foongus (SV09 10 -- JP SVM 009; English JTG/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="39720e3f-cbb2-5df9-ab1d-1d62e5b577c7",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=590,
    abilities=[
        Attack(
            title="Spore Ball",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
