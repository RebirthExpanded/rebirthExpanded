"""Purrloin (SV - White Flare 55/86 -- JP SV11W 052/086).

Basic Darkness. HP 60, weakness Grass x2, retreat 1, regulation mark I.

  Invite Evil  [D]  Search your deck for up to 3 Darkness Pokemon, reveal
                    them, and put them into your hand. Then, shuffle your
                    deck.

A three-card search into hand, so it is the shared search_to_hand with a
type filter: Darkness POKEMON, which is the live type of the card in the
deck -- a Pokemon that is Darkness only through an effect in play is not in
the deck to be found either way.

"Up to 3" is minimum=0. The empty-deck gate keeps the attack honest at the
one point where nothing could happen at all.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card, is_pokemon_of_type


def _darkness_pokemon(card) -> bool:
    return is_pokemon_card(card) and is_pokemon_of_type(card, PokemonTypes.DARKNESS)


card = PokemonCardDef(
    guid="d81dbfac-158b-5669-90c1-bfacf3444b93",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Invite Evil",
            game_text="Search your deck for up to 3 Darkness Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=search_to_hand(
                _darkness_pokemon, count=3, minimum=0,
                prompt="Choose up to 3 Darkness Pokémon to put into your hand."),
        ),
    ],
)
