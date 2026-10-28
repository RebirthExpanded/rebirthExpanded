"""Toxicroak (SV2 115 -- JP SV2D 041; English PAL/115). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6d22d6ec-2a14-547b-a0f9-c41b386eb458",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Pierce",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Knuckle Claws",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
