"""Heracross (ME6 1 -- JP M6 001; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5b699ea6-f3f4-5f04-b35e-85c2683e8bed",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Mega Horsepower",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=ac.recoil_attack(30),
        ),
    ],
)
