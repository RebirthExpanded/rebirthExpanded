"""Random Receiver (BW - Dark Explorers 99/108 -- JP "MDB" deck 036).

Item.

  "Reveal cards from the top of your deck until you reveal a Supporter
   card. Put it into your hand. Shuffle the other cards back into your
   deck."

Every card turned over is shown to BOTH players (reveal_cards reaches
each viewer the card is hidden from); the Supporter then goes to the
hand and the rest are shuffled back. With no Supporter in the deck the
whole deck is revealed and shuffled.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_supporter_card


async def random_receiver(ctx):
    deck = list(reversed(ctx.deck()))          # top first
    revealed = []
    found = None
    for card in deck:
        revealed.append(card)
        if is_supporter_card(card):
            found = card
            break
    if revealed:
        await ctx.reveal_cards(revealed)
    if found is not None:
        await ctx.put_in_hand([found], reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="d6a9dedd-7209-59f0-a8a6-9731d6063846",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver", "Item", "RandomReceiver"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=random_receiver,
)
