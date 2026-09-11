"""Therapeutic Energy (SV - Paldea Evolved 193/193 -- JP SV2D 071/071).

Special Energy.  "As long as this card is attached to a Pokemon, it
provides [C] Energy. The Pokemon this card is attached to recovers from
being Asleep, Confused, or Paralyzed and can't be affected by those
Special Conditions."
"""

from spirit.game.attributes import PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.data_utils import EnergyCardDef

_CURED = (SpecialConditions.ASLEEP, SpecialConditions.CONFUSED, SpecialConditions.PARALYZED)


async def therapeutic_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is None:
        return
    for condition in _CURED:
        await ctx.cure_condition(pokemon, condition)


card = EnergyCardDef(
    guid="dcede855-24bc-5ac6-80a2-85240821003b",
    key="SV2",
    name="Therapeutic Energy",
    display_name="Therapeutic Energy",
    searchable_by=["Therapeutic Energy", "Special", "TherapeuticEnergy"],
    subtypes=["Special"],
    collector_number=193,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    regulation_mark="G",
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    passive=condition_immunity_passive(conditions=_CURED),
    on_attach=therapeutic_on_attach,
)
