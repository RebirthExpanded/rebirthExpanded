"""Torkoal (SV09 25 -- JP SVM 017; English JTG/25). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="3cf6e313-8669-539f-8f34-5b1d9296fdb2",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Live Coal",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Heat Blast",
            game_text="",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
