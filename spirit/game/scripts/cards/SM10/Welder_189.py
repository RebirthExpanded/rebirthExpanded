"""Welder (SM - Unbroken Bonds 189/214 -- JP SM10 091/095).

Supporter.

  "Attach up to 2 [R] Energy cards from your hand to 1 of your Pokemon. If
   you do, draw 3 cards."

Effect attachments, not the turn's manual attach, so they do not spend it.
"If you do" gates the draw on at least one card actually attached, and the
card is only offered with a [R] Energy in hand to attach.
The Energy comes from the hand, so it sets off "when you attach an Energy
card from your hand" effects (Skiploom's Solar Evolution) -- once Welder
is done, so its draw comes first (ruling).
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_fire_energy_card
from spirit.game.data_utils import SupporterCardDef


async def welder(ctx):
    energies = [c for c in ctx.hand() if is_fire_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Fire Energy cards to attach.")
    if not picks:
        return
    # A Pokemon hit by Primeval Beak can't take Energy from the hand.
    targets = [p for p in ctx.my_pokemon_in_play()
               if not ctx.session.turn_state.attach_restricted(p.entity_id)]
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to attach the Energy to")
    if target is None:
        return
    attached = 0
    for energy in picks:
        # From the hand, so "when you attach an Energy card from your hand"
        # watchers (Solar Evolution) see it -- after Welder has finished,
        # draw included (counts_as_attachment defers them).
        if await ctx.attach_energy(energy, target, counts_as_attachment=True):
            attached += 1
    if attached:
        await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="5e936645-f905-53ba-963f-a941ae57da5b",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Welder.Name",
    display_name="Welder",
    searchable_by=["Welder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=welder,
    condition=requires_hand(is_fire_energy_card, 1, exclude_self=False),
)
