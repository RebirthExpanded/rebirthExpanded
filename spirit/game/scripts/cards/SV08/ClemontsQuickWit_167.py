"""Clemont's Quick Wit (SV08 167 -- JP SV8 103; English SSP/167, SSP/229, SSP/243). Japanese art.
"""

from spirit.game.attributes import Rarities
from spirit.game.data_utils import SupporterCardDef

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])

from spirit.game.attributes import PokemonTypes


async def clemonts_quick_wit(ctx):
    for p in ctx.my_pokemon_in_play():
        if _of_type(p, PokemonTypes.LIGHTNING):
            await ctx.heal(60, p)


card = SupporterCardDef(
    guid="4c17d744-3aee-5bf3-9953-444596fee1d2",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClemontsQuickWit.Name",
    display_name="Clemont's Quick Wit",
    searchable_by=["Clemont's Quick Wit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=clemonts_quick_wit,
)
