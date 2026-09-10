"""Artazon (SV - Paldea Evolved 171/193).

Stadium.

  "Once during each player's turn, that player may search their deck for a
   Basic Pokemon that doesn't have a Rule Box and put it onto their Bench.
   Then, that player shuffles their deck."

Both players get their own use each turn, which is what a Stadium Ability
already is here. The filter is the printed one: a Basic with no Rule Box,
so Pokemon ex, V and their relatives stay in the deck -- has_rule_box
already knows the whole family.

The Ability wants a deck to search and a Bench slot to fill, or there is
nothing to do.
"""

from spirit.game.data_utils import (StadiumCardDef, Ability, Activations,
                                    has_rule_box)
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (search_to_bench,
                                                     requires_bench_space,
                                                     requires_deck)
from spirit.game.session.effects import is_basic_pokemon


def _basic_without_rule_box(card):
    return is_basic_pokemon(card) and not has_rule_box(card.archetype_id)


def _artazon_usable(board, player_id, pokemon=None):
    return (requires_deck()(board, player_id)
            and requires_bench_space(1)(board, player_id))


ARTAZON_ABILITY = Ability(
    title="Artazon",
    game_text=("Once during each player's turn, that player may search their "
               "deck for a Basic Pokémon that doesn't have a Rule Box and put "
               "it onto their Bench. Then, that player shuffles their deck."),
    activation=Activations.ONCE_PER_TURN,
    condition=_artazon_usable,
    effect=search_to_bench(
        predicate=_basic_without_rule_box,
        prompt="Choose a Basic Pokémon without a Rule Box to put onto your Bench.",
    ),
)

card = StadiumCardDef(
    guid="49abf9c0-fff5-516e-ae11-04a0beffb3c7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Artazon.Name",
    display_name="Artazon",
    searchable_by=["Artazon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=171,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    ability=ARTAZON_ABILITY,
)
