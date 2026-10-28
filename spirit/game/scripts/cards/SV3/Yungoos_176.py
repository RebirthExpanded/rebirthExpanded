"""Yungoos (SV3 176 -- JP SV1a 062; English OBF/176). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="224b5760-7346-55cb-a839-b429174fdfb7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    display_name="Yungoos",
    searchable_by=["Yungoos", "Basic"],
    subtypes=["Basic"],
    collector_number=176,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=734,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(10),
        ),
    ],
)
