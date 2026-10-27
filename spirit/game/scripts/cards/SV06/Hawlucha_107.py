"""Hawlucha (SV06 107 -- JP SV5a 046; English TWM/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _more_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) > ac.count_prizes_remaining("opponent")(ctx)


card = PokemonCardDef(
    guid="e63dea02-e490-54d4-bb67-b2625a94b0aa",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_more_left, 90),
        ),
    ],
)
