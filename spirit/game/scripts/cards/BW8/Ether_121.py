"""Ether (BW - Plasma Storm 121/135 -- JP BW6-Bc 055/059, the art here).

Item.

  "Reveal the top card of your deck. If that card is a basic Energy card,
   attach it to 1 of your Pokemon. If it is not a basic Energy card, return
   it to the top of your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_deck
from spirit.game.data_utils import ItemCardDef
from spirit.game.session.effects import is_basic_energy


async def ether(ctx):
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.reveal_cards([card])
    if not is_basic_energy(card):
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(card, target)


card = ItemCardDef(
    guid="295637fd-6c57-5f16-b687-0e03c03c865e",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ether.Name",
    display_name="Ether",
    searchable_by=["Ether", "Item"],
    subtypes=["Item"],
    collector_number=121,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    condition=requires_deck(1),
    effect=ether,
)
