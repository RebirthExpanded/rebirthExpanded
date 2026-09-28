"""Ethan's Adventure (SV - Destined Rivals 165/182 -- JP SV9a 063/063).

Supporter.

  "Search your deck for up to 3 in any combination of Ethan's Pokemon and
   Basic [R] Energy cards, reveal them, and put them into your hand. Then,
   shuffle your deck."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.session.effects import is_basic_energy, is_pokemon_card


def _pick(card) -> bool:
    if is_basic_energy(card):
        return energy_provides_type(card, PokemonTypes.FIRE.value)
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return is_pokemon_card(card) and name.startswith("Ethan's ")


async def ethans_adventure(ctx):
    picks = await ctx.search_deck(
        _pick, count=3, minimum=0,
        prompt="Choose up to 3 Ethan's Pokémon and Basic [R] Energy cards.")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="f7362f6a-492c-5bca-aaa0-8d941bec238f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EthansAdventure.Name",
    display_name="Ethan's Adventure",
    searchable_by=["Ethan's Adventure", "Supporter", "EthansAdventure"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=ethans_adventure,
)
