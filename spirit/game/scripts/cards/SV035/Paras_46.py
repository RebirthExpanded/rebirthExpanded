"""Paras (SV035 46 -- JP SV2a 046; English MEW/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="745104d7-d5c2-5005-b8f5-39636284099c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    display_name="Paras",
    searchable_by=["Paras", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Spore Ball",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
