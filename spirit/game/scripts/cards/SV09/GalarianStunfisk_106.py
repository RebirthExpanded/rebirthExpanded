"""Galarian Stunfisk (SV09 106 -- JP SVM 085; English JTG/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c56e4811-975c-5eeb-8948-fc039ec37358",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfisk.Name",
    display_name="Galarian Stunfisk",
    searchable_by=["Galarian Stunfisk", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=618,
    abilities=[
        Attack(
            title="Mud-Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Bounding Bite",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=ac.recoil_attack(30),
        ),
    ],
)
