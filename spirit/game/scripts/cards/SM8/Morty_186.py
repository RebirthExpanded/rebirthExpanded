"""Morty (SM - Lost Thunder 186/214 -- JP SM7b 054/060).

Supporter.

  "You can play this card only if 1 of your [P] Pokemon was Knocked Out
   during your opponent's last turn.
   Your opponent reveals their hand. Choose 2 cards you find there. Your
   opponent shuffles those cards into their deck."

The playability clause reads the knockout ledger by the KO'd card's
printed type -- a Psychic Pokemon, however it was Knocked Out. With their
hand at 1 card, that one goes; with it empty the reveal shows nothing.
"""

import json

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.data_utils import SupporterCardDef, _attr_value, def_for


def _lost_psychic_pokemon_last_turn(board, player_id) -> bool:
    turn_state = getattr(board, "turn_state", None)
    for entry in (turn_state.pokemon_lost_last_turn(player_id) if turn_state else []):
        definition = def_for(entry.get("archetype_id"))
        if definition is None:
            continue
        raw = _attr_value(definition, AttrID.POKEMON_TYPES, "[]")
        types = json.loads(raw) if isinstance(raw, str) else list(raw or [])
        if PokemonTypes.PSYCHIC.value in types:
            return True
    return False


async def morty(ctx):
    hand = await ctx.reveal_hand(ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, min(2, len(hand)), minimum=min(2, len(hand)),
        prompt="Choose 2 cards to shuffle into your opponent's deck.")
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = SupporterCardDef(
    guid="1ecd9351-0910-5f9e-82b5-b42857c95ce3",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morty.Name",
    display_name="Morty",
    searchable_by=["Morty", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=morty,
    condition=_lost_psychic_pokemon_last_turn,
)
