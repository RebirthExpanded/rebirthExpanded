"""Ferroseed (RSV10PT5 68 -- JP SV11W 063; English WHT/148, WHT/68). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="1482f28a-10b6-51f2-8e9b-05dc933ec787",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    display_name="Ferroseed",
    searchable_by=["Ferroseed", "Basic"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=597,
    abilities=[
        Attack(
            title="Zzzt",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title="Metal Claw",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
