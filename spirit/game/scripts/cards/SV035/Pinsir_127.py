"""Pinsir (SV035 127 -- JP SV2a 127; English MEW/127). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _more_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) > ac.count_prizes_remaining("opponent")(ctx)


card = PokemonCardDef(
    guid="91f6c40a-aa99-5b6d-9933-6cdef21ebcd4",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Reckless Throw",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_more_left, 90),
        ),
    ],
)
