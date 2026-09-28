"""Impact Energy (SWSH - Chilling Reign 157/198).

Special Energy.

  "This card can only be attached to a Single Strike Pokemon. If this card
   is attached to anything other than a Single Strike Pokemon, discard this
   card."
  "As long as this card is attached to a Pokemon, it provides every type of
   Energy but provides only 1 Energy at a time. The Pokemon this card is
   attached to can't be Poisoned, and if it is already Poisoned, it
   recovers from that Special Condition."

Single Strike Energy's restriction, Rainbow Energy's type list, and
Therapeutic Energy's cure-on-attach plus condition immunity.
"""

from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import condition_immunity_passive


def is_single_strike(pokemon) -> bool:
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


async def impact_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is not None:
        await ctx.cure_condition(pokemon, SpecialConditions.POISONED)


card = EnergyCardDef(
    guid="4e7a1516-dba1-584a-9479-a0f41bc58742",
    key="SWSH6",
    name="Impact Energy",
    display_name="Impact Energy",
    searchable_by=["Impact Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=157,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_single_strike,
    discard_if_invalid=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=condition_immunity_passive(SpecialConditions.POISONED),
    on_attach=impact_on_attach,
)
