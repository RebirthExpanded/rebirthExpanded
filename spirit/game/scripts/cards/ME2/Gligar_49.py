"""Gligar (ME2 49 -- JP M2 043; English PFL/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e99ac08b-3baf-50d7-a759-2bd8fd52c714",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=207,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
