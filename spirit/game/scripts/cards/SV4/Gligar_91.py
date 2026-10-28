"""Gligar (SV4 91 -- JP SV3a 022; English PAR/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="84fbc92e-04b1-5864-9b39-cb7b17c59825",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    display_name="Gligar",
    searchable_by=["Gligar", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=207,
    abilities=[
        Attack(
            title="Toxic",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 2 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)
