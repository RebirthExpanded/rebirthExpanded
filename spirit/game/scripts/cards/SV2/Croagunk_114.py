"""Croagunk (SV2 114 -- JP SV2D 040; English PAL/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c727bd76-c73d-5107-af54-a9c6b295dc5f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
