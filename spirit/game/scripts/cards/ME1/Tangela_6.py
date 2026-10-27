"""Tangela (ME1 6 -- JP M1S 001; English MEG/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="0dd22fc9-fc8a-5557-8126-4d30a712e5f4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Attack(
            title="Poison Powder",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Hook",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
