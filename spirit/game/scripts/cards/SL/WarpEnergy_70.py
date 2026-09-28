"""Warp Energy (SM - Shining Legends 70/73 -- JP SM3+ 072/072).

Special Energy.  "This card provides [C] Energy. When you attach this card
from your hand to your Active Pokemon, switch that Pokemon with 1 of your
Benched Pokemon."

Jet Energy (SV2)'s shape turned around: the hand attach to the Active
switches it out, the player choosing the Benched Pokemon. The switch is not
optional; with an empty Bench nothing happens.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import EnergyCardDef


async def warp_energy_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is None or not is_in_active_spot(pokemon):
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to switch in") or bench[0]
    await ctx.switch_active(ctx.player_id, target)


card = EnergyCardDef(
    guid="38967c5d-dd3a-527b-98b2-321714892647",
    key="SL",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special", "WarpEnergy"],
    subtypes=["Special"],
    collector_number=70,
    set_code="SL",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=warp_energy_on_attach,
)
