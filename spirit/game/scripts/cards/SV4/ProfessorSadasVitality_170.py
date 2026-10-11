"""Professor Sada's Vitality (SV - Paradox Rift 170/182 -- JP SV4K 064/066).

Supporter.

  "Choose up to 2 of your Ancient Pokemon and attach a Basic Energy card
   from your discard pile to each of them. If you attached any Energy in
   this way, draw 3 cards."

Playable only with an Ancient Pokemon in play and a Basic Energy card in
the discard pile -- otherwise the card would do nothing (ruling: it can't
be played with no Basic Energy in the discard). The draw comes only after
an attachment, and each chosen Pokemon takes its own pick.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.session.effects import is_basic_energy


def _ancient(pokemon) -> bool:
    return "Ancient" in subtypes_for(pokemon.archetype_id)


def _sada_condition(board, player_id) -> bool:
    """An Ancient Pokemon in play and a Basic Energy card in the discard."""
    if not any(_ancient(p) for p in board.pokemon_in_play(player_id)):
        return False
    discard = board.find_player_area(player_id, "discard")
    return any(is_basic_energy(c) for c in (discard.children if discard else []))


async def professor_sadas_vitality(ctx):
    ancients = [p for p in ctx.my_pokemon_in_play() if _ancient(p)]
    attached = False
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
            if picks and await ctx.attach_energy(picks[0], target):
                attached = True
    if attached:
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
    condition=_sada_condition,
    effect=professor_sadas_vitality,
)
