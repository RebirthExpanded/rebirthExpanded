"""Dusk Stone (SM - Unbroken Bonds 167/214 -- JP SM10 084/095, the art
here).

Item.

  "Choose 1 of your Pokemon that evolves into Mismagius, Honchkrow,
   Chandelure, or Aegislash (including Pokemon-GX). Search your deck for a
   card that evolves from that Pokemon and put it onto that Pokemon to
   evolve it. Then, shuffle your deck. (You can use this card during your
   first turn or on a Pokemon that was put into play this turn.)"

The evolution goes through ctx.evolve_pokemon (Rare Candy's path), which
ignores the may-evolve turn rules, as the card says. A Pokemon that
evolves into one of the four is one whose evolutions in the deck carry
one of those names (Misdreavus, Murkrow, Lampent, Doublade).
"""

from spirit.game.attributes import AttrID, Rarities
from spirit.game.data_utils import ItemCardDef, def_for, evolves_from
from spirit.game.session.effects import is_pokemon_card

_TARGET_NAMES = ("Mismagius", "Honchkrow", "Chandelure", "Aegislash")


def _dusk_evolution(card) -> bool:
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_pokemon_card(card) and any(name.startswith(t) for t in _TARGET_NAMES)


def _dusk_evolutions_in_deck(board, player_id, pokemon):
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    if not logic_name:
        return []
    deck = board.find_player_area(player_id, "deck")
    return [c for c in (deck.children if deck else [])
            if _dusk_evolution(c) and evolves_from(c.archetype_id, logic_name)]


def _candidates(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if _dusk_evolutions_in_deck(board, player_id, p)]


def dusk_stone_playable(board, player_id) -> bool:
    return bool(_candidates(board, player_id))


async def dusk_stone(ctx):
    candidates = _candidates(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon to evolve with Dusk Stone")
    if target is None:
        return
    picks = await ctx.search_deck(
        lambda c: c in _dusk_evolutions_in_deck(ctx.board, ctx.player_id, target),
        count=1, minimum=0, prompt="Choose a card to evolve that Pokémon into.")
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="a185ca21-35dc-5d2d-ac4c-d0bb417e5a76",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskStone.Name",
    display_name="Dusk Stone",
    searchable_by=["Dusk Stone", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=dusk_stone_playable,
    effect=dusk_stone,
)
