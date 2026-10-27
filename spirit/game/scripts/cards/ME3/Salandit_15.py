"""Salandit (ME3 15 -- JP M3 015; English POR/15). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7abca073-1855-5d19-aae3-688cd06e4633",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Fire Claws",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
