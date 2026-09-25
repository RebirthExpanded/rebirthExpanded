"""Energy Recycle System (SM - Celestial Storm 128/168 -- JP SM6b 052/066).

Item.

  "Choose 1:
   - Put a basic Energy card from your discard pile into your hand.
   - Shuffle 3 basic Energy cards from your discard pile into your deck."

The JP text shows the cards to the opponent either way. With fewer than 3
basic Energy cards in the discard pile the shuffle takes all of them
(Special Charge's reading of a flat "Shuffle N"); the card needs at least
one to be played.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef


async def energy_recycle_system(ctx):
    energies = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energies:
        return
    choice = await ctx.choose(
        "Energy Recycle System: choose 1",
        ["Put a basic Energy card from your discard pile into your hand",
         "Shuffle 3 basic Energy cards from your discard pile into your deck"])
    if choice == 1:
        take = min(3, len(energies))
        picks = energies if len(energies) <= 3 else await ctx.choose_cards(
            energies, take, minimum=take,
            prompt="Choose 3 basic Energy cards to shuffle into your deck")
        if picks:
            await ctx.reveal_cards(picks, to_player=ctx.opponent_id)
            await ctx.shuffle_into_deck(picks)
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a basic Energy card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = ItemCardDef(
    guid="c551da86-57c7-5041-8495-8d476a23f9d2",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item", "EnergyRecycleSystem"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_basic_energy_card, 1),
    effect=energy_recycle_system,
)
