"""Steel Shelter (JP XY Hyper Metal Chain Deck 60 -- HMC 017/018; English
print XY - Phantom Forces 105/119).

Stadium.

  "Each [M] Pokemon (both yours and your opponent's) can't be affected by
   any Special Conditions. (Remove any Special Conditions affecting those
   Pokemon.)"

The come-into-play effect cures every [M] Pokemon on both sides; the
passive keeps them immune while the Stadium stands.
"""

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.data_utils import StadiumCardDef


def _is_metal_pokemon(pokemon) -> bool:
    return PokemonTypes.METAL.value in (
        pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _metal_protected(target, carrier) -> bool:
    return _is_metal_pokemon(target)


async def steel_shelter(ctx):
    for pid in (ctx.player_id, ctx.opponent_id):
        for pokemon in list(ctx.board.pokemon_in_play(pid)):
            if _is_metal_pokemon(pokemon):
                await ctx.cure_all_conditions(pokemon)


card = StadiumCardDef(
    guid="e7aefb9d-d8e8-5ab0-8555-e9846437af07",
    key="HMC",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name",
    display_name="Steel Shelter",
    searchable_by=["Steel Shelter", "Stadium", "SteelShelter"],
    subtypes=["Stadium"],
    collector_number=17,
    set_code="HMC",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=_metal_protected),
    effect=steel_shelter,
)
