"""Lilligant (ZSV10PT5 7 -- JP SV11B 007; English BLK/7, BLK/92). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="83f1a5cd-abe4-5735-82ac-7d1c4ec9c164",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Bemusing Aroma",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed and Poisoned. If tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, SpecialConditions.POISONED, flip=True, tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
        Attack(
            title="Cut",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
