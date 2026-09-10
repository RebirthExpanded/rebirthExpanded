"""Guzma & Hala (SM - Cosmic Eclipse 193/236).

Supporter, TAG TEAM.

  "Search your deck for a Stadium card, reveal it, and put it into your
   hand. Then, shuffle your deck."
  "When you play this card, you may discard 2 other cards from your hand.
   If you do, you may also search for a Pokemon Tool card and a Special
   Energy card in this way."

The Stadium half is unconditional; the discard buys the other two slots.
So unlike Quick Ball or Mysterious Treasure, where the discard is a gate
and refusing it ends the card, refusing here still fetches the Stadium.
The offer only appears when the hand can actually pay -- 2 cards, and
"other" is free: _execute_play_trainer moves this card to the trainer slot
before the effect runs, so it is not in hand to be picked.

Both halves are one browser through search_deck_groups, the way Arven and
Irida do it, with one labelled slot per group. The paid version simply
opens with three slots instead of one. search_deck_groups flushes queued
choreography first, so the two discarded cards are visibly gone before the
deck opens.

The pool's first TAG TEAM Supporter, which makes it the first card
Tag Call can find that is not a Pokemon -- no change needed there, since
Tag Call reads the subtype rather than asking for a Pokemon.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import (
    is_pokemon_tool, is_special_energy, is_stadium_card,
)

_STADIUM_SLOT = (is_stadium_card, 1, "playmat.prompt.selectastadiumcard")
_TOOL_SLOT = (is_pokemon_tool, 1, "playmat.prompt.selectapoketoolcard")
_ENERGY_SLOT = (is_special_energy, 1, "playmat.prompt.select1specialenergy")


async def guzma_and_hala(ctx):
    """Always a Stadium; discard 2 to also take a Tool and a Special Energy."""
    paid = False
    if len(ctx.hand()) >= 2 and await ctx.ask_yes_no(
            "Discard 2 cards to also search for a Pokémon Tool "
            "and a Special Energy card?"):
        paid = len(await ctx.discard_from_hand(
            2, minimum=2, prompt="Choose 2 cards to discard")) >= 2
    groups = [_STADIUM_SLOT] + ([_TOOL_SLOT, _ENERGY_SLOT] if paid else [])
    prompt = ("Choose a Stadium card, a Pokémon Tool card and a Special "
              "Energy card" if paid else "Choose a Stadium card")
    found = await ctx.search_deck_groups(groups, prompt=prompt)
    picks = [card for group in found for card in group]
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="fdd971e0-c437-596c-a49a-0a92d7b95d86",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM", "GuzmaHala"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=193,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=guzma_and_hala,
)
