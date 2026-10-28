"""Quaxly (SV2 49 -- JP SV1a 027; English PAL/206, PAL/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="87b2ccb9-94ab-550a-82aa-cdae43dddd74",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    display_name="Quaxly",
    searchable_by=["Quaxly", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=912,
    abilities=[
        Attack(
            title="Apply Gel",
            game_text="During your opponent's next turn, if the Defending Pokémon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ac.smokescreen_attack(),
        ),
    ],
)
