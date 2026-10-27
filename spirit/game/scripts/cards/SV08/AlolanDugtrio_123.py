"""Alolan Dugtrio (SV08 123 -- JP SV8 077; English SSP/123, SSP/208). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _three(ctx) -> bool:
    return len(ctx.hand()) == 3


card = PokemonCardDef(
    guid="0ccc7d45-eef1-554c-9621-4f3df95e51d6",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=123,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Trio-Cheehoo",
            game_text="If you don't have exactly 3 cards in your hand, this attack does nothing.",
            cost={},
            damage=120,
            effect=ac.bonus_if(_three, 0, else_nothing=True),
        ),
    ],
)
