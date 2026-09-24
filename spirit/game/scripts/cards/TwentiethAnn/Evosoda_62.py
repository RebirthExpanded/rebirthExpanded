"""Evosoda (Generations 62/83 -- JP 20th-anniversary Starter Pack 053/072).

Item.

  "Search your deck for a card that evolves from 1 of your Pokemon and put
   it onto that Pokemon. (This counts as evolving that Pokemon.) Shuffle
   your deck afterward. You can't use this card during your first turn or
   on a Pokemon that was put into play this turn."

Wally with the two timing rules kept: not on either player's first turn,
and only onto a Pokemon that has been in play since an earlier turn. The
evolution-availability gate applies (every copy of the evolution in
public zones = no target).
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import evolves_from, pokemon_can_still_evolve
from spirit.game.data_utils import ItemCardDef


def _evosoda_targets(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None or turn_state.turn_number <= 2:
        return []
    return [p for p in board.pokemon_in_play(player_id)
            if turn_state.entered_play_turn.get(p.entity_id) != turn_state.turn_number
            and pokemon_can_still_evolve(board, player_id, p)]


def _evosoda_condition(board, player_id):
    return bool(_evosoda_targets(board, player_id))


async def evosoda(ctx):
    candidates = _evosoda_targets(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return
    picks = await ctx.search_deck(
        lambda c, name=logic_name: evolves_from(c, name),
        count=1, minimum=0,
        prompt="Choose a card that evolves from that Pokémon.")
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="484d5933-2e8a-515c-977c-e7b75ec0fcff",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name",
    display_name="Evosoda",
    searchable_by=["Evosoda", "Item"],
    subtypes=["Item"],
    collector_number=62,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    condition=_evosoda_condition,
    effect=evosoda,
)
