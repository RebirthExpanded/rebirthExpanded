"""Draw Energy (SM - Cosmic Eclipse 209/236 -- JP SM11a 060/064).

Special Energy.

  "This card provides [C] Energy.
   When you attach this card from your hand to a Pokemon, draw a card."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef


async def draw_energy_on_attach(ctx):
    await ctx.draw_cards(1)


card = EnergyCardDef(
    guid="2320a5dd-5e0b-5dae-8de2-cf55fe42b9db",
    key="SM12",
    name="Draw Energy",
    display_name="Draw Energy",
    searchable_by=["Draw Energy", "Special", "DrawEnergy"],
    subtypes=["Special"],
    collector_number=209,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    on_attach=draw_energy_on_attach,
)
