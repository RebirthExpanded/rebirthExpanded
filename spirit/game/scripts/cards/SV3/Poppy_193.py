"""Poppy (SV3 193 -- JP SV3 105; English OBF/193, OBF/220, OBF/227). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

def _two_mons(board, player_id, card=None) -> bool:
    return len(board.pokemon_in_play(player_id)) >= 2


async def poppy(ctx):
    mine = ctx.my_pokemon_in_play()
    holders = [p for p in mine if ctx.attached_energies(p)]
    if not holders:
        return
    source = await ctx.choose_pokemon(holders, "Choose 1 of your Pokémon to move Energy from")
    if source is None:
        return
    dests = [p for p in mine if p is not source]
    dest = await ctx.choose_pokemon(dests, "Choose a Pokémon to move the Energy to") if dests else None
    if dest is None:
        return
    pool = list(ctx.attached_energies(source))
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Energy to move")
    for e in picks:
        await ctx.move_energy(e, dest)


card = SupporterCardDef(
    guid="3459c7ed-0719-5215-a251-8b6ef067cd04",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Poppy.Name",
    display_name="Poppy",
    searchable_by=["Poppy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    condition=_two_mons,
    effect=poppy,
)
