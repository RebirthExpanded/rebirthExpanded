"""Lillipup (RSV10PT5 74 -- JP SV11W 072; English WHT/154, WHT/74). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="fd8c6e4a-21ca-50ee-8a59-ae9640b0a9eb",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
