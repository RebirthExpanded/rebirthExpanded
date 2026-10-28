"""Houndstone (SV3 101 -- JP SV3 054; English OBF/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _two_or_four(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) in (2, 4)


card = PokemonCardDef(
    guid="330e8a9e-34f7-5bde-9390-ffc3418f756b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Rear Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Two Four-ocious",
            game_text="If your opponent has exactly 2 or 4 Prize cards remaining, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_two_or_four, 120),
        ),
    ],
)
