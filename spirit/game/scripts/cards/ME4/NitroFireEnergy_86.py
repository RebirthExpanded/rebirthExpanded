"""Nitro Fire Energy (ME - Chaos Rising 86 -- JP M4 081).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [R] Energy.
   If this card is discarded by an effect of an attack used by the [R]
   Pokemon this card is attached to, put this card into your hand after
   attack damage and effects."

Boomerang Energy's on_discarded_by_carrier_attack hook (it already runs
after the attack's damage and effects), returning the card to hand.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type


async def nitro_fire_return(ctx, energy, pokemon):
    if pokemon is None or not is_pokemon_of_type(pokemon, PokemonTypes.FIRE):
        return
    if energy._containing_area_name() == "discard":
        await ctx.put_in_hand([energy], reveal=True)


card = EnergyCardDef(
    guid="cf23047a-ebcc-50f1-b6c6-501b2fc57741",
    key="ME4",
    name="Nitro Fire Energy",
    display_name="Nitro Fire Energy",
    searchable_by=["Nitro Fire Energy", "Special", "NitroFireEnergy"],
    subtypes=["Special"],
    collector_number=86,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.FIRE,
    is_special=True,
    provides=[[PokemonTypes.FIRE]],
    on_discarded_by_carrier_attack=nitro_fire_return,
)
