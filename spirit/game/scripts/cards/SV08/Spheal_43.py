"""Spheal (SV08 43 -- JP SV8 027; English SSP/199, SSP/43). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8406d2cb-ce74-5b69-aa7c-f7eeac22ea5a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    display_name="Spheal",
    searchable_by=["Spheal", "Basic"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
