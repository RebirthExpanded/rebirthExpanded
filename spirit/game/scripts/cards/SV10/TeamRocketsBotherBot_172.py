"""Team Rocket's Bother-Bot (SV10 172 -- JP SV10 087; English DRI/172). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef

import random

from spirit.game.attributes import GameSequence


async def _bother_bot(ctx):
    """Turn 1 of your opponent's face-down Prize cards face up and choose a
    random card from your opponent's hand. Your opponent reveals that card.
    You may have your opponent switch those cards. (That Prize card remains
    face up for the rest of the game.)

    The Prize turned up is a blind pick (Lunatic Sense / Blazer); after a
    switch the hand card sits face up in that slot."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    prizes = [c for c in (prize_area.children if prize_area else [])
              if not getattr(c, "face_up_prize", False)]
    prize = None
    if prizes:
        idx = await ctx.choose(
            "Turn which of your opponent's Prize cards face up?",
            [str(i + 1) for i in range(len(prizes))]) if len(prizes) > 1 else 0
        prize = prizes[idx or 0]
        await ctx.flush_choreography()
        prize.face_up_prize = True
        await session.send_game_sequence(
            list(session.players.values()), GameSequence.GROUPED_MOVE,
            [session._entity_introduced_msg(prize)])
    hand = ctx.board.find_player_area(ctx.opponent_id, "hand")
    cards = list(hand.children) if hand else []
    if not cards:
        return
    pick = random.choice(cards)
    await ctx.reveal_cards([pick])
    await ctx.flush_choreography()
    if prize is None or not await ctx.ask_yes_no(
            "Have your opponent switch the revealed card with the face-up Prize card?"):
        return
    slot = prize.board_slot if prize.board_slot is not None else prize_area.children.index(prize)
    prize.face_up_prize = False
    await ctx.put_in_hand([prize], reveal=True)
    await ctx.flush_choreography()
    if not ctx.board.move_card(pick.entity_id, prize_area.entity_id, slot):
        return
    pick.face_up_prize = True
    await session.send_game_sequence(
        list(session.players.values()), GameSequence.GROUPED_MOVE,
        [session._entity_introduced_msg(pick),
         session._entity_moved_msg(pick.entity_id, prize_area.entity_id, slot)])
    await session.send_game_sequence(
        list(session.players.values()), GameSequence.GROUPED_MOVE,
        [session._refresh_prize_gaps(ctx.opponent_id, prize_area)])


card = ItemCardDef(
    guid="9f221b20-c579-5c91-bff1-e4727100ddb4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsBotherBot.Name",
    display_name="Team Rocket's Bother-Bot",
    searchable_by=["Team Rocket's Bother-Bot", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=_bother_bot,
)
