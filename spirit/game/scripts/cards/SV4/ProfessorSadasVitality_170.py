"""Professor Sada's Vitality (SV - Paradox Rift 170/182 -- JP SV4K 064/066).

Supporter.

  "Choose up to 2 of your Ancient Pokemon and attach a Basic Energy card
   from your discard pile to each of them. Then, draw 3 cards."

The draw is unconditional; the attach half needs Ancient Pokemon in play
and Basic Energy in the discard pile, and each chosen Pokemon takes its
own pick.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.session.effects import is_basic_energy


def _ancient(pokemon) -> bool:
    return "Ancient" in subtypes_for(pokemon.archetype_id)


async def professor_sadas_vitality(ctx):
    ancients = [p for p in ctx.my_pokemon_in_play() if _ancient(p)]
    if ancients and any(is_basic_energy(c) for c in ctx.discard_pile()):
        targets = await ctx.choose_cards(
            ancients, 2, minimum=0,
            prompt="Choose up to 2 of your Ancient Pokémon")
        for target in targets:
            energies = [c for c in ctx.discard_pile() if is_basic_energy(c)]
            if not energies:
                break
            picks = await ctx.choose_cards(
                energies, 1, minimum=1,
                prompt="Choose a Basic Energy card from your discard pile to attach")
            if picks:
                await ctx.attach_energy(picks[0], target)
    await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="766db587-bb52-5dc9-82e2-c4388cafa88c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSadasVitality.Name",
    display_name="Professor Sada's Vitality",
    searchable_by=["Professor Sada's Vitality", "Supporter", "ProfessorSadasVitality"],
    subtypes=["Supporter"],
    collector_number=170,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=professor_sadas_vitality,
)
