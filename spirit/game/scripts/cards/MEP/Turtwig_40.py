"""Turtwig (MEP 40 -- JP MP 110; English MEP/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c5b569c8-2b44-5df2-8ff7-0305477ad6d9",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=387,
    abilities=[
        Attack(
            title="Razor Leaf",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
