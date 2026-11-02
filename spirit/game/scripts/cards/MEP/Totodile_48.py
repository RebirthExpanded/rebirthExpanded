"""Totodile (MEP 48 -- JP MP 106; English MEP/48). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="5271807e-36f8-54a7-b26a-006416054f62",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    display_name="Totodile",
    searchable_by=["Totodile", "Basic"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=158,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
