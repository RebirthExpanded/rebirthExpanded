"""Hypno (ME6 30 -- JP M6 030; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c1fe5f87-e89c-5cf6-9485-a4426764b5f4",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Mind Ruler",
            game_text="This attack does 20 damage for each card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("opponent"), 20),
        ),
        Attack(
            title="Hypnotic Wave",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
