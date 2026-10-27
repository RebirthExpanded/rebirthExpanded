"""Shroomish (SV10 5 -- JP MC 027; English DRI/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="4b64af54-cf1a-5438-98d5-a09099f77627",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    display_name="Shroomish",
    searchable_by=["Shroomish", "Basic"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=285,
    abilities=[
        Attack(
            title="Rolling Tackle",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
