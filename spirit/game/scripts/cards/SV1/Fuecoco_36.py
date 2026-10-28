"""Fuecoco (SV1 36 -- JP SVAL 002; English SVI/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9706ad4b-d4da-5987-a7b9-108964be946f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Gnaw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Combustion",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
