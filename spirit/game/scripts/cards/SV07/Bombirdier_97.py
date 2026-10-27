"""Bombirdier (SV07 97 -- JP SVI 038; English SCR/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="73557861-c247-5dea-95f5-0a137a66f49a",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bombirdier.Name",
    display_name="Bombirdier",
    searchable_by=["Bombirdier", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=962,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ac.recoil_attack(20),
        ),
    ],
)
