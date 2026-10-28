"""Grimer (SV1 126 -- JP SV1S 051; English SVI/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="abddcb83-5c1a-5e95-933d-8c8ff9dd3c58",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=88,
    abilities=[
        Attack(
            title="Super Poison Breath",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
