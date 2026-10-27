"""Emma (ME4 77 -- JP M4 078; English CRI/107, CRI/77). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def emma(ctx):
    hand = ctx.hand(ctx.opponent_id)
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    n = sum(1 for c in hand if is_pokemon_card(c))
    if n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="b40e2b1c-efff-519d-abea-68a46e79ac6f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Emma.Name",
    display_name="Emma",
    searchable_by=["Emma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=emma,
)
