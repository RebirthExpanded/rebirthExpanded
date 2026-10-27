"""Rabsca (SV08 14 -- JP SV8 009; English SSP/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


def _thin_deck(ctx) -> bool:
    return len(ctx.deck()) <= 3


card = PokemonCardDef(
    guid="9a421006-28ef-5d52-84e5-374876a86b80",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(3),
        ),
        Attack(
            title="Counterturn",
            game_text="If there are 3 or fewer cards in your deck, this attack does 200 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.bonus_if(_thin_deck, 200),
        ),
    ],
)
