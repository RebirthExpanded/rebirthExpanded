"""Twist Mountain (BW - Dark Explorers 101/108 -- JP BW4 069/069, the art here).

Stadium.

  "Once during each player's turn, that player may flip a coin. If heads,
   the player puts a Restored Pokemon from their hand onto their Bench."

Restored Pokemon (Tirtouga, Archen and the rest) cannot be played from
the hand at all, so this is one of the two ways they reach the Bench;
tails spends the use for the turn.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.data_utils import Ability, Activations, StadiumCardDef, subtypes_for


def _is_restored(card) -> bool:
    return "Restored" in subtypes_for(card.archetype_id)


def _condition(board, player_id, stadium=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_restored(c) for c in hand.children):
        return False
    return requires_bench_space(1)(board, player_id, stadium)


async def twist_mountain(ctx):
    pool = [c for c in ctx.hand() if _is_restored(c)]
    if not pool:
        return
    if not (await ctx.flip_coins(1, "Twist Mountain"))[0]:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a Restored Pokémon to put onto your Bench.")
    for card in picks:
        await ctx.bench_pokemon(card)


ABILITY = Ability(
    title="Twist Mountain",
    game_text="Once during each player's turn, that player may flip a coin. If heads, the player puts a Restored Pokémon from their hand onto their Bench.",
    activation=Activations.ONCE_PER_TURN,
    effect=twist_mountain,
    condition=_condition,
)

card = StadiumCardDef(
    guid="cc36d61c-288a-5ab6-bb26-689bb814788c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TwistMountain.Name",
    display_name="Twist Mountain",
    searchable_by=["Twist Mountain", "Stadium", "TwistMountain"],
    subtypes=["Stadium"],
    collector_number=101,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    ability=ABILITY,
)
