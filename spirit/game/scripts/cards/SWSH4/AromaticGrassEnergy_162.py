"""Aromatic Grass Energy (SWSH - Vivid Voltage 162/185 -- JP S3a 074/076).

Special Energy.

  "As long as this card is attached to a Pokemon, it provides [G] Energy.
   The [G] Pokemon this card is attached to recovers from all Special
   Conditions and can't be affected by any Special Conditions."

Bubbly Water Energy (ME4)'s shape: a Grass holder is cured when the card is
attached and is immune to Special Conditions while it stays attached.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.session.passives import carrier_pokemon


def _grass_holder(target, carrier):
    if carrier_pokemon(carrier) is not target:
        return False
    return PokemonTypes.GRASS.value in (target.get_attribute(AttrID.POKEMON_TYPES) or [])


async def aromatic_grass_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is None:
        return
    if PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
        await ctx.cure_all_conditions(pokemon)


card = EnergyCardDef(
    guid="7082710f-138c-56dd-895f-7bddbfe68231",
    key="SWSH4",
    name="Aromatic Grass Energy",
    display_name="Aromatic Grass Energy",
    searchable_by=["Aromatic Grass Energy", "Special", "AromaticGrassEnergy"],
    subtypes=["Special"],
    collector_number=162,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    on_attach=aromatic_grass_on_attach,
    passive=condition_immunity_passive(protects=_grass_holder),
)
