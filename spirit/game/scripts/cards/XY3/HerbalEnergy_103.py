"""Herbal Energy (XY - Furious Fists 103/111 -- JP XY3 095/096).

Special Energy.

  "This card can only be attached to [G] Pokemon. This card provides [G]
   Energy only while this card is attached to a [G] Pokemon. When you
   attach this card from your hand to 1 of your [G] Pokemon, heal 30 damage
   from that Pokemon. (If this card is attached to anything other than a
   [G] Pokemon, discard this card.)"

Strong Energy (XY3)'s type-locked shape: attach_to + discard_if_invalid.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.data_utils import EnergyCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _grass_pokemon(pokemon) -> bool:
    return is_pokemon_of_type(pokemon, PokemonTypes.GRASS)


async def herbal_on_attach(ctx):
    pokemon = ctx.attached_to
    if pokemon is not None and _grass_pokemon(pokemon):
        await ctx.heal(30, pokemon)


card = EnergyCardDef(
    guid="22b566a5-3973-53ad-8e4f-30f5c554f6e3",
    key="XY3",
    name="Herbal Energy",
    display_name="Herbal Energy",
    searchable_by=["Herbal Energy", "Special", "HerbalEnergy"],
    subtypes=["Special"],
    collector_number=103,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.GRASS,
    is_special=True,
    attach_to=_grass_pokemon,
    discard_if_invalid=True,
    provides=[[PokemonTypes.GRASS]],
    on_attach=herbal_on_attach,
)
