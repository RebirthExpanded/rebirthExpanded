"""Phione (SM - Cosmic Eclipse 57/236 -- JP SM11a 022/064).

Basic Water Pokemon. HP 70, weakness Grass x2, retreat 1.

  Ability  Whirlpool Suction  Once during your turn (before your attack),
                              if this Pokemon is on your Bench, you may have
                              your opponent switch their Active Pokemon with
                              1 of their Benched Pokemon. If you do, discard
                              all cards attached to this Pokemon and put it
                              on the bottom of your deck.
  Rain Splash  [W] 10

THEY choose which Benched Pokemon comes up, so this is a switch and not a
gust: the chooser opens on their side. With an empty Bench opposite there is
nothing to switch to, so the ability does nothing at all -- and, "if you do"
being the gate on the second sentence, this Pokemon stays where it is rather
than paying the cost for free.

The cost itself is paid in full: everything attached is discarded, and the
Pokemon goes UNDER the deck rather than into the discard, so it can be drawn
again.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import full_stack


def _opposing_bench(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return []
    bench = board.find_player_area(opponent, "bench")
    return list(bench.children) if bench else []


def _benched_with_opposing_bench(board, player_id, pokemon) -> bool:
    """On your Bench, and with something on theirs to switch to."""
    return (not is_in_active_spot(pokemon)) and bool(
        _opposing_bench(board, player_id))


async def whirlpool_suction(ctx):
    """They switch; if they did, this Pokemon pays for it."""
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    chosen = await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon.", player_id=ctx.opponent_id)
    if chosen is None:
        return
    if not await ctx.switch_active(ctx.opponent_id, chosen):
        return
    attached = [c for c in full_stack(ctx.source) if c is not ctx.source]
    if attached:
        await ctx.discard_cards(attached)
    await ctx.put_on_bottom_of_deck(ctx.source)


card = PokemonCardDef(
    guid="23a2e56f-95e6-5270-838d-5f2a5c7da1d8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=489,
    abilities=[
        Ability(
            title="Whirlpool Suction",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may have your opponent switch their Active Pokémon with 1 of their Benched Pokémon. If you do, discard all cards attached to this Pokémon and put it on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_benched_with_opposing_bench,
            effect=whirlpool_suction,
        ),
        Attack(
            title="Rain Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
