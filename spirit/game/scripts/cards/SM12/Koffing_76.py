"""Koffing (SM - Cosmic Eclipse 76/236 -- JP SM11b 026/049).

Basic Psychic Pokemon. HP 60, weakness Psychic x2, retreat 1.

  Ability  Blow-Away Bomb  Once during your turn, when you discard this
                           Pokemon with the effect of Roxie, you may put 1
                           damage counter on each of your opponent's
                           Pokemon. (Place damage counters after the effect
                           of Roxie.)
  Poison Gas  [PC] 10  Your opponent's Active Pokemon is now Poisoned.

The Ability names one Supporter and nothing else opens its window: a hand
discarded to Ultra Ball, milled off the deck or knocked out in play does
none of this. Roxie fires it after its own draw, which is the parenthetical.
"""

from spirit.game.attributes import (PokemonStage, PokemonTypes, Rarities,
                                    SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import blow_away_bomb
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers

card = PokemonCardDef(
    guid="3e8cfd21-c59b-5fd3-841d-b53f5c08f564",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Ability(
            title="Blow-Away Bomb",
            game_text="Once during your turn, when you discard this Pokémon with the effect of Roxie, you may put 1 damage counter on each of your opponent's Pokémon. (Place damage counters after the effect of Roxie.)",
            trigger=Triggers.ON_DISCARDED_BY_ROXIE,
            effect=blow_away_bomb,
        ),
        Attack(
            title="Poison Gas",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
