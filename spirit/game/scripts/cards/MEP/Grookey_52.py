"""Grookey (MEP 52 -- JP MP 122; English MEP/52). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="31ed0f6b-aa45-5272-912a-e47f74380902",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    display_name="Grookey",
    searchable_by=["Grookey", "Basic"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Branch Poke",
            game_text="",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
    ],
)
