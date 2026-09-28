"""Tulip (SV - Paradox Rift 181/182 -- JP SV4M 066/066).

Supporter.

  "Put up to 4 in any combination of [P] Pokemon and basic [P] Energy cards
   from your discard pile into your hand."

The JP text has them shown to the opponent. Not playable with neither in
the discard pile.
"""

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_pokemon_card


def _is_psychic(card) -> bool:
    return PokemonTypes.PSYCHIC.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


def _tulip_target(card) -> bool:
    return (is_pokemon_card(card) or is_basic_energy_card(card)) and _is_psychic(card)


async def tulip(ctx):
    cards = [c for c in ctx.discard_pile() if _tulip_target(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, min(4, len(cards)), minimum=1,
        prompt="Choose up to 4 Psychic Pokémon and basic Psychic Energy cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = SupporterCardDef(
    guid="f16559b3-6439-5ea8-bf51-4d6d1489f1d9",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tulip.Name",
    display_name="Tulip",
    searchable_by=["Tulip", "Supporter", "Tulip"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=requires_discard(_tulip_target, 1),
    effect=tulip,
)
