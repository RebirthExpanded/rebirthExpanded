from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


def _carmine_condition(board, player_id, card=None) -> bool:
    # Only offered during turn 1 (client-side legality still allows players to
    # click it, so the effect re-checks "go first" as well).
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number == 1 and ts.active_player_id == player_id


async def carmine_effect(ctx):
    """If you go first, discard your hand and draw 5."""
    # We can't fully gate "go first" at legality-check time (conditions don't
    # have ctx), so we enforce it here.
    if getattr(ctx.session, "first_player_id", None) != ctx.player_id:
        return
    if ctx.session.turn_state.turn_number != 1:
        return

    await ctx.discard_cards(list(ctx.hand()))
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="a01d0152-bdda-4c8a-8fc1-327fef2a0cdb",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Carmine.Name",
    display_name="Carmine",
    searchable_by=["Carmine", "Supporter", "Carmine"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    condition=_carmine_condition,
    effect=carmine_effect,
)

