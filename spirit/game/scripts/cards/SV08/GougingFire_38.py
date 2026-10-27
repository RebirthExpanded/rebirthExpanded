"""Gouging Fire (SV08 38 -- JP SV7a 009; English SSP/38, SVP/151). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _four_or_less(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) <= 4


card = PokemonCardDef(
    guid="6a6198a9-9cb6-598b-bb75-4179f6097cba",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFire.Name",
    display_name="Gouging Fire",
    searchable_by=["Gouging Fire", "Basic", "Ancient"],
    subtypes=["Basic", "Ancient"],
    collector_number=38,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=1020,
    abilities=[
        Attack(
            title="Lunge Out",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Blazing Charge",
            game_text="If your opponent has 4 or fewer Prize cards remaining, this attack does 70 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_four_or_less, 70),
        ),
    ],
)
