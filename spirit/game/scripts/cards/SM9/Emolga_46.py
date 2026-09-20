"""Emolga (SM - Team Up 46/181 -- JP SM8a 009/052, the art here).

Basic Lightning Pokemon. HP 60, weakness Lightning x2, resistance
Fighting -20, retreat 0.

  Nuzzly Gathering  (Ability)  Once during your turn (before your attack),
                               you may search your deck for a Pokemon that
                               has the Nuzzle attack, reveal it, and put it
                               into your hand. Then, shuffle your deck.
  Nuzzle            [L]        Flip a coin. If heads, your opponent's Active
                               Pokemon is now Paralyzed.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, has_attack_titled
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_card

_has_nuzzle = has_attack_titled("Nuzzle")


def _nuzzle_pokemon(card) -> bool:
    return is_pokemon_card(card) and _has_nuzzle(card)


card = PokemonCardDef(
    guid="9f4c7cd5-a39a-5b0b-bf7f-1d00bd17e02a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=587,
    abilities=[
        Ability(
            title="Nuzzly Gathering",
            game_text="Once during your turn (before your attack), you may search your deck for a Pokémon that has the Nuzzle attack, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(_nuzzle_pokemon, count=1, minimum=0, reveal=True,
                                  prompt="Choose a Pokémon that has the Nuzzle attack."),
        ),
        Attack(
            title="Nuzzle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
