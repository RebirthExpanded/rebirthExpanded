"""Giacomo (SV085 138 -- JP SV2P 069; English PAL/182, PAL/252, PAL/267, PRE/138). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.session.effects import is_special_energy


async def giacomo(ctx):
    for p in list(ctx.opponent_pokemon_in_play()):
        pool = [e for e in ctx.attached_energies(p) if is_special_energy(e)]
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Special Energy to discard")
            await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="8af54d69-e26a-5f12-9e08-5dd224a4fd2a",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giacomo.Name",
    display_name="Giacomo",
    searchable_by=["Giacomo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=giacomo,
)
