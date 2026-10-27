"""Skorupi (ME3 51 -- JP M3 050; English POR/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="428352fc-370c-566d-9bd0-db121b204162",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    display_name="Skorupi",
    searchable_by=["Skorupi", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=451,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
