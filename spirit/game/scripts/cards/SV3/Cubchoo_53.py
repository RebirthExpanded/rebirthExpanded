"""Cubchoo (SV3 53 -- JP SV3 026; English OBF/53). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5bda3135-c298-545f-afc7-ae3de960118d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo", "Basic"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=613,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Trip Over",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
