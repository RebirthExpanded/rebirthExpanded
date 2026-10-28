"""Giovanni's Charisma (SV035 161 -- JP SV2a 162; English MEW/161, MEW/197, MEW/204). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_energy_card


def _charisma_condition(board, player_id, card=None) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    d = board.active_pokemon(other) if other else None
    from spirit.game.models.board import EnergyEntity
    return d is not None and any(isinstance(c, EnergyEntity) for c in d.children)


async def giovannis_charisma(ctx):
    d = ctx.opponent_active()
    if d is None or not ctx.attached_energies(d):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy to put into your opponent's hand")
    if not picks:
        return
    before = picks[0].parent
    await ctx.put_in_hand(picks)
    if picks[0].parent is before:
        return
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    mine = ctx.board.active_pokemon(ctx.player_id)
    if pool and mine is not None:
        choice = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach to your Active Pokémon")
        if choice:
            await ctx.attach_energy(choice[0], mine)


card = SupporterCardDef(
    guid="80b8128b-01c8-5495-9e46-06910cb03f52",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisCharisma.Name",
    display_name="Giovanni's Charisma",
    searchable_by=["Giovanni's Charisma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_charisma_condition,
    effect=giovannis_charisma,
)
