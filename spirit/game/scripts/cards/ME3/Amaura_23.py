"""Amaura (ME3 23 -- JP M3 022; English POR/23). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5f587a82-25dd-564b-9b9f-1169e3c9321e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name",
    display_name="Amaura",
    searchable_by=["Amaura", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueSailFossil.Name",
    family_id=698,
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
