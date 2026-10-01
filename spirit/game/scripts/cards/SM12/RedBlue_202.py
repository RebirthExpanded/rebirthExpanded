"""Red & Blue (SM - Cosmic Eclipse 202/236 -- JP SM12 090/095).

Supporter.

  "Search your deck for a Pokemon-GX that evolves from 1 of your Pokemon
   and put it onto that Pokemon to evolve it. Then, shuffle your deck.
   (You can't use this card during your first turn or on a Pokemon that
   was put into play this turn.)
   When you play this card, you may discard 2 other cards from your hand.
   If you do, search your deck for up to 2 basic Energy cards and attach
   them to the Pokemon you evolved in this way."

The 2 cards are paid when the card is played, before anything else.
A Pokemon this Supporter's effects can't reach (Ariados's Trapping
Thread) can still be chosen, but it doesn't evolve: the Pokemon-GX found
for it is discarded, and with nothing evolved no Energy is attached
(ruling).
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.session.effects import is_basic_energy, is_pokemon_card
from spirit.game.session.passives import own_trainer_effect_blocked


def _evolvable(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None:
        return []
    return [p for p in board.pokemon_in_play(player_id)
            if turn_state.may_evolve_target(p.entity_id)
            and p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)]


def _red_and_blue_condition(board, player_id, card=None) -> bool:
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and bool(_evolvable(board, player_id))


def _gx_from(logic_name):
    def pred(card) -> bool:
        return (is_pokemon_card(card) and "GX" in subtypes_for(card.archetype_id)
                and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic_name)
    return pred


async def red_and_blue(ctx):
    paid = False
    if len(ctx.hand()) >= 2 and await ctx.ask_yes_no(
            "Discard 2 other cards from your hand to attach up to 2 basic Energy "
            "from your deck to the Pokémon you evolve?"):
        paid = len(await ctx.discard_from_hand(2, prompt="Discard 2 cards for Red & Blue")) == 2
    candidates = _evolvable(ctx.board, ctx.player_id)
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve") if candidates else None
    if target is None:
        await ctx.shuffle_deck()
        return
    picks = await ctx.search_deck(
        _gx_from(target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)), count=1, minimum=0,
        prompt="Choose a Pokémon-GX that evolves from it.")
    evolved = None
    if picks:
        if own_trainer_effect_blocked(ctx.board, target, ctx.source):
            # Trapping Thread: it can't be evolved by this card; the
            # Pokemon-GX goes to the discard pile.
            await ctx.discard_cards(picks)
        else:
            await ctx.evolve_pokemon(target, picks[0])
            evolved = picks[0]
    if paid and evolved is not None:
        energies = await ctx.search_deck(
            is_basic_energy, count=2, minimum=0,
            prompt="Choose up to 2 basic Energy cards to attach.")
        for energy in energies:
            await ctx.attach_energy(energy, evolved)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="6fb9c367-2b47-5b86-8cd2-039881ec089d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedBlue.Name",
    display_name="Red & Blue",
    searchable_by=["Red & Blue", "Supporter", "RedBlue"],
    subtypes=["Supporter"],
    collector_number=202,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    condition=_red_and_blue_condition,
    effect=red_and_blue,
)
