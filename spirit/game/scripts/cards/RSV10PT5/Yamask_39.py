"""Yamask (RSV10PT5 39 -- JP SV11W 036; English WHT/122, WHT/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ac69765e-bb3e-5285-8849-8ee8bee85e71",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=562,
    abilities=[
        Attack(
            title="Focused Wish",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(20),
        ),
    ],
)
