"""Jet Energy (SV - Paldea Evolved 190/193 -- JP SV1a 072/073).

Special Energy.  "As long as this card is attached to a Pokemon, it
provides [C] Energy. When you attach this card from your hand to 1 of your
Benched Pokemon, switch that Pokemon with your Active Pokemon."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import EnergyCardDef


async def jet_energy_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is None or is_in_active_spot(pokemon):
        return
    await ctx.switch_active(ctx.player_id, pokemon)


card = EnergyCardDef(
    guid="ef988193-5321-5dfb-8a2a-4fc795195e22",
    key="SV2",
    name="Jet Energy",
    display_name="Jet Energy",
    searchable_by=["Jet Energy", "Special", "JetEnergy"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=jet_energy_on_attach,
)
