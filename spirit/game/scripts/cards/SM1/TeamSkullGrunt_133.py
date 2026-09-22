"""Team Skull Grunt (SM - Sun & Moon 133/149 -- JP SMA 055/059, the art here).

Supporter.

  "Your opponent reveals their hand. Discard 2 Energy cards you find there."

The reveal is the ordinary hand browser; YOU pick which two Energy go,
so the chooser opens on this player's side over their opponent's hand.
Fewer than 2 Energy there: every one of them is discarded.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.data_utils import SupporterCardDef

DISCARD = 2


async def team_skull_grunt(ctx):
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    energy = [c for c in hand if is_energy_card(c)]
    if not energy:
        return
    take = min(DISCARD, len(energy))
    picks = await ctx.choose_cards(
        energy, take, minimum=take, player_id=ctx.player_id,
        prompt="Choose 2 Energy cards to discard from your opponent's hand.")
    await ctx.discard_cards(picks or energy[:take])


card = SupporterCardDef(
    guid="5fd1a59a-6df3-5697-a97b-7f7d5bf1f915",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamSkullGrunt.Name",
    display_name="Team Skull Grunt",
    searchable_by=["Team Skull Grunt", "Supporter", "TeamSkullGrunt"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=team_skull_grunt,
)
