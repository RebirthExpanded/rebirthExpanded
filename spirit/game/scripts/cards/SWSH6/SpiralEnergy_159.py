"""Spiral Energy (SWSH - Chilling Reign 159/198).

Special Energy.

  "This card can only be attached to a Rapid Strike Pokemon. If this card
   is attached to anything other than a Rapid Strike Pokemon, discard this
   card."
  "As long as this card is attached to a Pokemon, it provides every type of
   Energy but provides only 1 Energy at a time. The Pokemon this card is
   attached to can't be Paralyzed, and if it is already Paralyzed, it
   recovers from that Special Condition."

Impact Energy with the Rapid Strike restriction and Paralysis in place of
Poison.
"""

from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.card_effects.passives_common import condition_immunity_passive


def is_rapid_strike(pokemon) -> bool:
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


async def spiral_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is not None:
        await ctx.cure_condition(pokemon, SpecialConditions.PARALYZED)


card = EnergyCardDef(
    guid="864d97da-55bc-5a68-95d2-6f0c01b5dce9",
    key="SWSH6",
    name="Spiral Energy",
    display_name="Spiral Energy",
    searchable_by=["Spiral Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=159,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=is_rapid_strike,
    discard_if_invalid=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=condition_immunity_passive(SpecialConditions.PARALYZED),
    on_attach=spiral_on_attach,
)
