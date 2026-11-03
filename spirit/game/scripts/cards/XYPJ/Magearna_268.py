"""Magearna (XYPJ 268 -- JP XYP 268; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="cbbe734b-290f-5f30-93de-95a8ca2e4071",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic"],
    subtypes=["Basic"],
    collector_number=268,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Attack(
            title="Assist Gear",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=su.search_to_hand(is_item_card, count=1, reveal=True, prompt="Choose an Item card."),
        ),
        Attack(
            title="Gear Smash",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.METAL: 3},
            damage=50,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)
