"""Cyndaquil (MEP 47 -- JP MP 105; English MEP/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="e35465d7-7b50-5929-9e5d-56755cd88131",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    display_name="Cyndaquil",
    searchable_by=["Cyndaquil", "Basic"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Tackle",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
