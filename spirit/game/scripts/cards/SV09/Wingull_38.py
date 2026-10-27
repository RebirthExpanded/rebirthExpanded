"""Wingull (SV09 38 -- JP SVM 032; English JTG/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="5cd86a46-273c-561b-b1a3-7235c72b5185",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    display_name="Wingull",
    searchable_by=["Wingull", "Basic"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=278,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
