"""Gabite (BW - Dragons Exalted 89/124 -- JP Garchomp Deck 30 006/015, the
art here).

Stage 1 Dragon Pokemon (evolves from Gible). HP 80, weakness Dragon x2,
no resistance, retreat 1.

  Dragon Call  (Ability)  Once during your turn (before your attack), you
                          may search your deck for a [N] Pokemon, reveal
                          it, and put it into your hand. Shuffle your deck
                          afterward.
  Dragonslice  [WF] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _dragon_pokemon(card) -> bool:
    return is_pokemon_of_type(card, PokemonTypes.DRAGON)


card = PokemonCardDef(
    guid="88606ded-f7ab-56ce-acf8-7ed546db97ea",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=444,
    abilities=[
        Ability(
            title="Dragon Call",
            game_text="Once during your turn (before your attack), you may search your deck for a [N] Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(_dragon_pokemon, count=1, minimum=0, reveal=True,
                                  prompt="Choose a [N] Pokémon to put into your hand."),
        ),
        Attack(
            title="Dragonslice",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
