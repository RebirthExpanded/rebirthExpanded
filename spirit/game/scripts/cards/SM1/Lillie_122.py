"""Lillie (SM - Sun & Moon 122/149 -- JP SM7 092/096, the art here).

Supporter.

  "Draw cards until you have 6 cards in your hand. If it's your first turn,
   draw cards until you have 8 cards in your hand."

Under current rules the player going first cannot play a Supporter on
their first turn, so "your first turn" can only be the second player's
first turn -- turn 2 of the game (house ruling; the 8-card case dates from
when the first player could).
The JP SM7 reprint has no English Celestial Storm print, so the card sits
at its original Sun & Moon number.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import second_players_first_turn
from spirit.game.data_utils import SupporterCardDef


async def lillie(ctx):
    first_turn = second_players_first_turn(ctx.board, ctx.player_id)
    await ctx.draw_until(8 if first_turn else 6)


card = SupporterCardDef(
    guid="43f67cc6-3536-5876-8894-846f904aa4b5",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=lillie,
)
