"""Pikachu (Promo_SWSH 234 -- JP SP 272; English SP/234). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.session.effects import is_item_card


async def _gift_delivery(ctx):
    if (await ctx.flip_coins(1, "Gift Delivery"))[0]:
        await su.search_to_hand(is_item_card, reveal=True, prompt="Choose an Item card.")(ctx)


card = PokemonCardDef(
    guid="e9994784-7f17-5b88-a18e-7c08b78a85dd",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=234,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Gift Delivery",
            game_text="Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_gift_delivery,
        ),
        Attack(
            title="Pika Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
