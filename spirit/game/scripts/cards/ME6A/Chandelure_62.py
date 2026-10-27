"""Chandelure (ME6A 62 -- JP M6a 062; English 30C/137, 30C/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dbf480f6-17e1-57e4-b7c4-d34a3cb124da",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=62,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=ac.condition_attack(SpecialConditions.BURNED, SpecialConditions.CONFUSED),
        ),
    ],
)
