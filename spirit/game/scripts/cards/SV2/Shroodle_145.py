"""Shroodle (SV2 145 -- JP SV2D 054; English PAL/145). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c9bcc656-83fc-5709-af89-586f3c395aa7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
