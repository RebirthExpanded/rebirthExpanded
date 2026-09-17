"""Brock's Grit (SM - Team Up 135/181 -- JP SM9 087/095, the art here).

Supporter.

  "Shuffle 6 in any combination of Pokemon and basic Energy cards from
   your discard pile into your deck."

Super Rod's filter at a flat 6. Flat, per the Q&A: with six or more such
cards in the discard the full 6 must go back (no stopping at 5); with
fewer, all of them go, and a single Pokemon in the discard is enough to
play it. The picks are shown to the opponent on the way (the Japanese
print says so outright), then the deck is shuffled.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.card_effects.trainers import pokemon_or_basic_energy
from spirit.game.data_utils import SupporterCardDef


def _is_pokemon_or_basic_energy(card) -> bool:
    return bool(pokemon_or_basic_energy([card]))


async def brocks_grit(ctx):
    """Shuffle exactly 6 (or all, if fewer) Pokemon / basic Energy back."""
    candidates = [c for c in ctx.discard_pile() if _is_pokemon_or_basic_energy(c)]
    if not candidates:
        return
    if len(candidates) <= 6:
        picks = list(candidates)
    else:
        picks = await ctx.choose_cards(
            candidates, 6, minimum=6,
            prompt="Choose 6 Pokémon and/or basic Energy cards to shuffle into your deck.",
        )
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks)


card = SupporterCardDef(
    guid="aca0ac0c-b1b9-5a2d-adc6-e2c223ba375c",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter", "BrocksGrit"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    condition=requires_discard(_is_pokemon_or_basic_energy, 1),
    effect=brocks_grit,
)
