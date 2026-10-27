"""Gulpin (SV07 91 -- JP SV7 061; English SCR/154, SCR/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1dfa57ea-3312-51e5-addb-96e8369bfbd3",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name",
    display_name="Gulpin",
    searchable_by=["Gulpin", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=316,
    abilities=[
        Attack(
            title="Drool",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Super Poison Breath",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
