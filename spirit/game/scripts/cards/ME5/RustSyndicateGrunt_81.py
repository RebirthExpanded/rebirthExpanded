"""Rust Syndicate Grunt (ME - PBL 81 -- JP M5 077, the art here).

Supporter.

  "You can play this card only if any of your Pokemon were Knocked Out
   during your opponent's last turn."
  "Discard an Energy from 1 of your opponent's Pokemon."

The revenge clause is Rosa's (ally_ko_last_turn: every knockout, not
only ones an attack dealt); the discard reaches their Bench too.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.data_utils import SupporterCardDef


def _opponent_energies(board, player_id):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return []
    return [c for p in board.pokemon_in_play(opponent)
            for c in p.children if is_energy_card(c)]


def _playable(board, player_id, card=None) -> bool:
    return ally_ko_last_turn(board, player_id) \
        and bool(_opponent_energies(board, player_id))


async def rust_syndicate_grunt(ctx):
    targets = _opponent_energies(ctx.board, ctx.player_id)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, 1, minimum=1,
        prompt="Choose an Energy to discard from your opponent's Pokémon")
    await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="8e99a7e4-9d78-56c3-a939-964267062087",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RustSyndicateGrunt.Name",
    display_name="Rust Syndicate Grunt",
    searchable_by=["Rust Syndicate Grunt", "Supporter", "RustSyndicateGrunt"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_playable,
    effect=rust_syndicate_grunt,
)
