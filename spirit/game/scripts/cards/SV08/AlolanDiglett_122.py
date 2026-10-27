"""Alolan Diglett (SV08 122 -- JP SV8 076; English SSP/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="1c947cb6-1ade-51a2-8448-680873c35c4d",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=50,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=30,
            effect=ac.flip_or_nothing(),
        ),
    ],
)
