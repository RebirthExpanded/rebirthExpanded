"""Drowzee (SV035 96 -- JP SV2a 096; English MEW/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b6c21ba8-ac1a-5a86-b946-d5fec1844d61",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=96,
    abilities=[
        Attack(
            title="Zen Headbutt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
