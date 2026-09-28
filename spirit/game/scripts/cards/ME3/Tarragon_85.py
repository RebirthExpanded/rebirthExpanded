"""Tarragon (ME - Perfect Order 85 -- JP M3 073).

Supporter.

  "Put up to 4 in any combination of [F] Pokemon and Basic [F] Energy cards
   from your discard pile into your hand."
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import SupporterCardDef
from spirit.game.session.effects import is_basic_energy, is_pokemon_of_type


def _pick(card) -> bool:
    if is_basic_energy(card):
        return energy_provides_type(card, PokemonTypes.FIGHTING.value)
    return is_pokemon_of_type(card, PokemonTypes.FIGHTING)


def _has_target(board, player_id, card=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_pick(c) for c in discard.children)


async def tarragon(ctx):
    pool = [c for c in ctx.discard_pile() if _pick(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(4, len(pool)), minimum=1,
                                   prompt="Choose up to 4 [F] Pokémon and Basic [F] Energy cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = SupporterCardDef(
    guid="4ef0745b-12ce-5b85-84d2-aac871cf40eb",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tarragon.Name",
    display_name="Tarragon",
    searchable_by=["Tarragon", "Supporter", "Tarragon"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_has_target,
    effect=tarragon,
)
