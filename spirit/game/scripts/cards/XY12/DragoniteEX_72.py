"""Dragonite-EX (XY - Evolutions 72/108 -- JP CP6 070/087).

Basic Colorless Pokemon-EX. HP 180, weakness Lightning x2, resistance
Fighting -20, retreat 3.

  Ability  Pull Up  When you play this Pokemon from your hand onto your
                    Bench, you may put 2 Basic Pokemon (except Dragonite-EX)
                    from your discard pile into your hand.
  Hyper Beam  [CCCC] 130  Discard an Energy from your opponent's Active
                          Pokemon.

Pull Up is a "you may": the pick is optional and up to 2; the cards are
revealed on the way to the hand (the Japanese text says so).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers, def_for)
from spirit.game.session.effects import is_basic_pokemon


def _basic_not_dragonite_ex(card) -> bool:
    definition = def_for(card.archetype_id)
    return is_basic_pokemon(card) and \
        getattr(definition, "display_name", "") != "Dragonite-EX"


def _pull_up_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(_basic_not_dragonite_ex(c) for c in (discard.children if discard else []))


card = PokemonCardDef(
    guid="200ab5f0-db9c-5b54-91e3-446b6afe5819",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=72,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=147,
    abilities=[
        Ability(
            title="Pull Up",
            game_text="When you play this Pokémon from your hand onto your Bench, you may put 2 Basic Pokémon (except Dragonite-EX) from your discard pile into your hand.",
            trigger=Triggers.ON_PLAY,
            condition=_pull_up_condition,
            effect=recover_from_discard(
                _basic_not_dragonite_ex, count=2, minimum=0, reveal=True,
                prompt="Choose up to 2 Basic Pokémon to put into your hand"),
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=discard_opponent_energy_attack(count=1),
        ),
    ],
)
