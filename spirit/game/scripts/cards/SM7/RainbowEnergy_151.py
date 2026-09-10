"""Rainbow Energy (SM - Celestial Storm 151/168 -- JP SM6b 066/066).

Special Energy.

  "When you attach this card from your hand to 1 of your Pokemon, put 1
   damage counter on that Pokemon. This card provides every type of Energy
   but provides only 1 Energy at a time.

   While this card is not attached to a Pokemon, it provides [C] Energy."

The self-inflicted counter is an on_attach hook and fires only for a hand
attachment, which is exactly what the card says -- an effect that moves an
already-attached Rainbow (Weavile-GX, Replace) or one that attaches it from
the discard puts nothing on. It is a damage COUNTER, so no Weakness and no
shield reads it as an attack.

Aurora Energy's rainbow with no condition attached: the type list is
whatever it is holding, always, so nothing has to be re-read as the board
changes.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.passives import Passive, carrier_pokemon


class RainbowEnergyPassive(Passive):
    """Every type of Energy, one at a time, while it is on a Pokemon."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        return [[option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME]


async def rainbow_energy_on_attach(ctx):
    """A damage counter on whatever it lands on, from hand."""
    pokemon = ctx.attached_to
    if pokemon is None:
        return
    await ctx.deal_damage(10, target=pokemon, apply_modifiers=False,
                          as_counters=True)


card = EnergyCardDef(
    guid="2b6becc8-f2e9-5956-a576-20ad5ee3f834",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.energy.RainbowEnergy.Name",
    display_name="Rainbow Energy",
    searchable_by=["Rainbow Energy", "Special", "RainbowEnergy"],
    subtypes=["Special"],
    collector_number=151,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=RainbowEnergyPassive(),
    on_attach=rainbow_energy_on_attach,
)
