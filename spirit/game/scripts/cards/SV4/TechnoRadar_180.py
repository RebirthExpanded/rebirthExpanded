"""Techno Radar (SV - Paradox Rift 180/182 -- JP SV4M 060/066).

Item.  "You can use this card only if you discard another card from your
hand. Search your deck for up to 2 Future Pokemon, reveal them, and put
them into your hand. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import ItemCardDef, subtypes_for
from spirit.game.session.effects import is_pokemon_card


def _future_pokemon(card) -> bool:
    return is_pokemon_card(card) and "Future" in subtypes_for(card.archetype_id)


async def techno_radar(ctx):
    paid = await ctx.discard_from_hand(1, prompt="Discard a card for Techno Radar")
    if not paid:
        return
    picks = await ctx.search_deck(_future_pokemon, count=2, minimum=0,
                                  prompt="Choose up to 2 Future Pokémon to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="a1fba52a-657c-59b6-852a-5a2842854656",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnoRadar.Name",
    display_name="Techno Radar",
    searchable_by=["Techno Radar", "Item", "TechnoRadar"],
    subtypes=["Item"],
    collector_number=180,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    condition=requires_hand(None, 1),
    effect=techno_radar,
)
