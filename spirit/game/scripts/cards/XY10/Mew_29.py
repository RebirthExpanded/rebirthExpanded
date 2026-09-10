"""Mew (XY - Fates Collide 29/124 -- JP XY10 027/078).

Basic Psychic. HP 50, weakness Psychic x2, no retreat cost.

  Ability  Memories of Dawn  This Pokemon can use the attacks of any of
                             your Basic Pokemon in play. (You still need the
                             necessary Energy to use each attack.)

  Encounter  [C]  Search your deck for a Pokemon, reveal it, and put it into
                  your hand. Shuffle your deck afterward.

"Any of YOUR Basic Pokemon in play" -- both the Japanese text and the
English print say your side, so the opponent's Basics are out of reach;
Mew-EX's Versatile is the one that reaches across the table.

Itself excluded, of course: the borrowed-attacks passive skips the carrier,
which also keeps a board of two of these from feeding each other nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import (BorrowedAttacksPassive,
                                              own_pokemon_in_play)
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card

card = PokemonCardDef(
    guid="20217585-07d7-5e08-8cdc-e1914146e181",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Memories of Dawn",
            game_text="This Pokémon can use the attacks of any of your Basic Pokémon in play. (You still need the necessary Energy to use each attack.)",
            passive=BorrowedAttacksPassive(own_pokemon_in_play, is_basic_pokemon),
        ),
        Attack(
            title="Encounter",
            game_text="Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=0,
                                  prompt="Choose a Pokémon to put into your hand."),
        ),
    ],
)
