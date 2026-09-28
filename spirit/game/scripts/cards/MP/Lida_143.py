"""Lida (JP MEGA Promo 143 -- no English print yet).

Supporter.

  "You can use this card only if any of your Mega Evolution Pokemon ex were
   Knocked Out during your opponent's last turn. Search your deck for up to
   2 Basic Energy cards and attach them to 1 of your Mega Evolution Pokemon
   ex. Then, shuffle your deck."
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.session.effects import is_basic_energy


def _mega(pokemon) -> bool:
    return "SV_Mega" in subtypes_for(pokemon.archetype_id)


def _mega_lost_last_turn(board, player_id, card=None) -> bool:
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None:
        return False
    return any("SV_Mega" in subtypes_for(ko.get("archetype_id") or "")
               for ko in turn_state.pokemon_lost_last_turn(player_id))


_search = search_attach_energy(
    predicate=is_basic_energy, count=2, distribute=False, target_pred=_mega,
    prompt="Choose up to 2 Basic Energy cards to attach to 1 of your Mega Evolution Pokémon ex.")


card = SupporterCardDef(
    guid="f6c7cb48-7c9b-5fa2-9185-de2713ddc941",
    key="MP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lida.Name",
    display_name="Lida",
    searchable_by=["Lida", "Supporter", "Lida"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="MP",
    regulation_mark="J",
    rarity=Rarities.RarePromo,
    condition=_mega_lost_last_turn,
    effect=_search,
)
