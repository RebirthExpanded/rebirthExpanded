"""Misty's Vitality (ME - Abyss Eye 80 -- JP M5 075).

Supporter.

  "Search your deck for up to 4 Basic [W] Energy cards and attach them to 1
   of your Pokemon. Then, shuffle your deck. Your turn ends."

Kiawe's shape: the search-and-attach, then ctx.ends_turn.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_basic_energy


def _basic_water(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.WATER.value)


_search = search_attach_energy(
    predicate=_basic_water, count=4, distribute=False,
    prompt="Choose up to 4 Basic [W] Energy cards to attach to 1 of your Pokémon.")


async def mistys_vitality(ctx):
    await _search(ctx)
    ctx.ends_turn = True


card = SupporterCardDef(
    guid="de59f26f-58b2-5d0e-ad64-11b39cfcc2bb",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysVitality.Name",
    display_name="Misty's Vitality",
    searchable_by=["Misty's Vitality", "Supporter", "MistysVitality"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=mistys_vitality,
)
