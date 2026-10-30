"""Kiawe (SM - Burning Shadows 116/147 -- JP SM3H 049/051, the art here).

Supporter.

  "Search your deck for up to 4 Energy cards and attach them to 1 of your
   Pokemon. Then, shuffle your deck. Your turn ends."

All four go on ONE Pokemon (distribute=False), and the turn ends whether
or not any were found (Rotom Bike's ctx.ends_turn).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_energy_card

_search = search_attach_energy(
    predicate=is_energy_card, count=4, distribute=False,
    prompt="Choose up to 4 Energy cards to attach to 1 of your Pokémon.")


async def kiawe(ctx):
    await _search(ctx)
    ctx.ends_turn = True


card = SupporterCardDef(
    guid="130e957e-5c0a-5723-a7b3-98f01e283537",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=kiawe,
)
