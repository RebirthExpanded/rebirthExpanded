"""Chimecho (SM - Crimson Invasion 43/111 -- JP SM4S 023/050).

Basic Psychic. HP 70, weakness Psychic x2, retreat 1.

  Bell of Silence  [P] 10  Your opponent can't play any Pokemon that has an
                           Ability from their hand during their next turn.

The pool's play locks all named Trainers or Energy until now, so
legal_actions only asked about them for the fossils -- the Pokemon that are
Item cards in hand. It now asks of every card in hand, which is what lets
this lock (and Horror House GX's wider one) reach a Pokemon at all. Every
existing lock takes a predicate that says no to a Pokemon, so nothing else
moved.

"A Pokemon that has an Ability" is the printed Ability, read off the card
in hand, so an Ability lock on the board does not make one playable again:
Path to the Peak turns Abilities off in play, it does not unprint them.
Attacks are not Abilities, which is what has_printed_ability filters out.

The lock covers putting one onto the Bench and evolving into one, since
both are playing the card from hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card


def _pokemon_with_ability(card) -> bool:
    return is_pokemon_card(card) and has_printed_ability(card)


async def bell_of_silence(ctx):
    """10, then their Ability Pokemon stay in hand next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _pokemon_with_ability)


card = PokemonCardDef(
    guid="a7225473-fdf5-5629-994c-d0abf1a0ee11",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Bell of Silence",
            game_text="Your opponent can't play any Pokémon that has an Ability from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=bell_of_silence,
        ),
    ],
)
