"""Tepig (ME2PT5 29 -- JP MC 109; English ASC/29). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b7347f30-adca-5082-95ac-85ec7e420603",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
