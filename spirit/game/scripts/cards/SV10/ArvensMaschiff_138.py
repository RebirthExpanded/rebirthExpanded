"""Arven's Maschiff (SV10 138 -- JP SV9a 051; English DRI/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c3156cc9-3294-5ddc-a22d-4d78743c1716",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMaschiff.Name",
    display_name="Arven's Maschiff",
    searchable_by=["Arven's Maschiff", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=942,
    abilities=[
        Attack(
            title="Stampede",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
