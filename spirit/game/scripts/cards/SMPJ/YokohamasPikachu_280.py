"""Yokohama's Pikachu (SMPJ 280 -- JP SMP 280; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card

_deep_sea = ac.flip_or_nothing(then=su.recover_from_discard(is_item_card, count=1, reveal=True,
                                                            prompt="Choose an Item card to put into your hand."))


card = PokemonCardDef(
    guid="39289069-e1b7-5176-8b61-04f400e4fbe0",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YokohamasPikachu.Name",
    display_name="Yokohama's Pikachu",
    searchable_by=["Yokohama's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=280,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Deep Sea Exploration",
            game_text="Flip a coin. If heads, put an Item card from your discard pile into your hand, revealing it to your opponent.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_deep_sea,
        ),
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
