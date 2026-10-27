"""Meowstic (ME3 34 -- JP M3 033; English POR/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="e41d0c4f-e44f-5a47-8490-d2f9d92e8d5e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name",
    display_name="Meowstic",
    searchable_by=["Meowstic", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    family_id=677,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("defender"), 30, base=30),
        ),
    ],
)
