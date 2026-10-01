"""Rainbow Energy (SM - Celestial Storm 151/168 -- JP SM6b 066/066).

Special Energy.

  "When you attach this card from your hand to 1 of your Pokemon, put 1
   damage counter on that Pokemon. This card provides every type of Energy
   but provides only 1 Energy at a time.

   While this card is not attached to a Pokemon, it provides [C] Energy."

The self-inflicted counter is an ON_ENERGY_ATTACHED trigger the card grants
its holder, so it fires only for an attachment from the hand -- an effect
that moves an already-attached Rainbow (Weavile-GX, Replace) or attaches it
from the discard puts nothing on -- and is ordered with the attachment's
other triggers by the holder's owner: Skiploom's Solar Evolution first and
the Pokemon it was attached to is gone, so no counter (ruling). It is a damage COUNTER, so no Weakness and no
shield reads it as an attack.

Aurora Energy's rainbow with no condition attached: the type list is
whatever it is holding, always, so nothing has to be re-read as the board
changes.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers, def_for
from spirit.game.session.effects import special_energy_neutralized
from spirit.game.session.passives import Passive, carrier_pokemon


class RainbowEnergyPassive(Passive):
    """Every type of Energy, one at a time, while it is on a Pokemon."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or carrier_pokemon(energy) is not holder:
            return options
        return [[option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME]


NAME = "Rainbow Energy"


def _rainbow_applies(ctx) -> bool:
    """This Rainbow Energy, just attached from my hand to this Pokemon,
    which is still in play."""
    energy = ctx.attached_energy
    if energy is None or getattr(def_for(energy.archetype_id), "display_name", None) != NAME:
        return False
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return False
    if energy.parent is not ctx.source or special_energy_neutralized(energy):
        return False
    return ctx.source in ctx.board.pokemon_in_play(ctx.player_id)


async def rainbow_energy(ctx):
    """A damage counter on the Pokemon it was attached to from hand."""
    if _rainbow_applies(ctx):
        await ctx.deal_damage(10, target=ctx.source, apply_modifiers=False,
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
    granted_abilities=[
        Ability(
            title="Rainbow Energy",
            game_text="When you attach this card from your hand to 1 of your Pokémon, put 1 damage counter on that Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=rainbow_energy,
            trigger_applies=_rainbow_applies,
        ),
    ],
)
