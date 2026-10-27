"""Venipede (ZSV10PT5 54 -- JP SV11B 057; English BLK/132, BLK/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="417930dd-56ff-58c3-a075-52f41f847863",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    display_name="Venipede",
    searchable_by=["Venipede", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=543,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
