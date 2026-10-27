"""Meltan (SV07 102 -- JP SVI 040; English SCR/102). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="9de0cb6a-ddb6-5e94-b39a-2df56fb661e0",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    display_name="Meltan",
    searchable_by=["Meltan", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=808,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Beam",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
