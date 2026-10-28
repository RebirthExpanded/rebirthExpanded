"""Varoom (SVP 26 -- JP SV1S 059; English SVI/140, SVP/26). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f87d79a8-1a66-527b-a6fc-07df7b5dbb9b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title="Poison Gas",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
