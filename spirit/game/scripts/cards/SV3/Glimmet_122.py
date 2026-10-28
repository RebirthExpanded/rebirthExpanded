"""Glimmet (SV3 122 -- JP SV3 064; English OBF/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="d32920cb-ddc0-5af4-95fb-1137e7c0b95e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    display_name="Glimmet",
    searchable_by=["Glimmet", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=969,
    abilities=[
        Attack(
            title="Poison Shard",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
