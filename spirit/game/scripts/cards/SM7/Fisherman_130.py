"""Fisherman (SM - Celestial Storm 130/168 -- JP SM7 089/096).

Supporter.

  "Put 4 basic Energy cards from your discard pile into your hand."

The JP text shows them to the opponent. With fewer than 4, all of them come
back; the card needs at least one to be played.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import SupporterCardDef


async def fisherman(ctx):
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = energies if len(energies) <= 4 else await ctx.choose_cards(
        energies, 4, minimum=4, prompt="Choose 4 basic Energy cards to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = SupporterCardDef(
    guid="5c84f9de-ad9d-5fc9-be93-dd39a0e974e8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter", "Fisherman"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card, 1),
    effect=fisherman,
)
