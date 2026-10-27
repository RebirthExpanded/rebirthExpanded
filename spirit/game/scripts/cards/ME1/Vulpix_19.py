"""Vulpix (ME1 19 -- JP M1L 010; English MEG/138, MEG/19). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="406fda45-6a97-55ab-856b-18b5a94d6f40",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
