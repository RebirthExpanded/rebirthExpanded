"""Exeggcute (SV045 23 -- JP SVEM 002; English PAF/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="60633f12-868b-5df2-8a68-815f1eb45da8",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=102,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
