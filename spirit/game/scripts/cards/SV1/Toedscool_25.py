"""Toedscool (SV - Scarlet & Violet 25/198 -- JP SV1V 010/078).

Basic Grass Pokemon. HP 60, weakness Fire x2, retreat 2.

  Spore  [G]     Your opponent's Active Pokemon is now Asleep.
  Ram    [CC] 10
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="4859ad84-3458-5b16-b24d-5ea23d632e9d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    display_name="Toedscool",
    searchable_by=["Toedscool", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=948,
    regulation_mark="G",
    abilities=[
        Attack(title="Spore", game_text="Your opponent's Active Pokémon is now Asleep.",
               cost={PokemonTypes.GRASS: 1}, damage=0,
               effect=condition_attack(SpecialConditions.ASLEEP)),
        Attack(title="Ram", game_text="", cost={PokemonTypes.COLORLESS: 2}, damage=10),
    ],
)
