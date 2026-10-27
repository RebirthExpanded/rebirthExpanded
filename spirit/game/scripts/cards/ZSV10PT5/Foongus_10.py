"""Foongus (ZSV10PT5 10 -- JP SV11B 010; English BLK/10, BLK/95). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="925e5b67-a7d7-54d2-9f27-955bcfe57491",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=590,
    abilities=[
        Attack(
            title="Toxic Spore",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
