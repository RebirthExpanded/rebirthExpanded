"""Lance {*} (SM - Dragon Majesty 61/70 -- JP SM6a 051/053).

Supporter, Prism Star.

  "You can play this card only if 1 of your Pokemon was Knocked Out during
   your opponent's last turn.
   Search your deck for up to 2 [N] Pokemon and put them onto your Bench.
   Then, shuffle your deck."

Rosa's gate with a Bench search behind it: ally_ko_last_turn, then
search_to_bench with the Dragon filter, capped by the Bench space left.
Any stage -- "Dragon Pokemon", not "Basic". Prism Star's own rules come
from the subtype.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import ally_ko_last_turn
from spirit.game.card_effects.support_common import (requires_bench_space,
                                                      search_to_bench)
from spirit.game.card_effects.trainers import is_dragon_pokemon
from spirit.game.data_utils import SupporterCardDef


def _lance_condition(board, player_id) -> bool:
    return ally_ko_last_turn(board, player_id) and requires_bench_space(1)(board, player_id)


card = SupporterCardDef(
    guid="dc3ae9f7-94d2-5f18-9458-568a0ba1ebf1",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LancePrismStar.Name",
    display_name="Lance {*}",
    searchable_by=["Lance", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=61,
    set_code="DM",
    rarity=Rarities.Prism,
    effect=search_to_bench(
        is_dragon_pokemon, count=2,
        prompt="Choose up to 2 Dragon Pokémon to put onto your Bench."),
    condition=_lance_condition,
)
