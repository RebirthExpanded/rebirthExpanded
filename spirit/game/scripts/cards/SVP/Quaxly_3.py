"""Quaxly (SVP 3 -- JP SVP 215; English SVP/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="abb0ded4-ad2a-5767-91ed-d7caeaf586f4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    display_name="Quaxly",
    searchable_by=["Quaxly", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=912,
    abilities=[
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
