"""Miraidon ex (SV - Scarlet & Violet 81/198 -- JP SV1V 037/078).

Basic Lightning Pokemon ex. HP 220, weakness Fighting x2, retreat 1.

  Ability  Tandem Unit  Once during your turn, you may search your deck
                        for up to 2 Basic [L] Pokemon and put them onto
                        your Bench. Then, shuffle your deck.
  Photon Blaster  [LLC] 220  During your next turn, this Pokemon can't
                             attack.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import requires_deck, search_to_bench
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_of_type
from spirit.game.session.passives import effective_bench_capacity


def _basic_lightning(card) -> bool:
    return is_basic_pokemon(card) and is_pokemon_of_type(card, PokemonTypes.LIGHTNING)


def _tandem_unit_condition(board, player_id, pokemon=None) -> bool:
    bench = board.find_player_area(player_id, "bench")
    return requires_deck(1)(board, player_id) and \
        len(bench.children if bench else []) < effective_bench_capacity(board, player_id)


card = PokemonCardDef(
    guid="5c97f66b-273e-585e-96f7-2027b6dc300e",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Miraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=81,
    set_code="SV1",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    regulation_mark="G",
    abilities=[
        Ability(title="Tandem Unit",
                game_text="Once during your turn, you may search your deck for up to 2 Basic [L] Pokémon and put them onto your Bench. Then, shuffle your deck.",
                activation=Activations.ONCE_PER_TURN, condition=_tandem_unit_condition,
                effect=search_to_bench(predicate=_basic_lightning, count=2,
                                       prompt="Choose up to 2 Basic [L] Pokémon to put onto your Bench.")),
        Attack(title="Photon Blaster", game_text="During your next turn, this Pokémon can't attack.",
               cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1}, damage=220,
               locks_next_turn=True),
    ],
)
