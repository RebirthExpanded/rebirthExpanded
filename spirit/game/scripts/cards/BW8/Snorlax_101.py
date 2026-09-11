"""Snorlax (BW - Plasma Storm 101/135 -- JP BW7-B 054/070).

Team Plasma Basic Colorless Pokemon. HP 130, weakness Fighting x2,
retreat 4.

  Ability  Block  As long as this Pokemon is your Active Pokemon, your
                  opponent's Active Pokemon can't retreat.
  Teamact  [CCCCC] 30x  Does 30 damage times the number of Team Plasma
                        Pokemon you have in play.

The pool's first Team Plasma Pokemon: the "Team Plasma" subtype is what
Teamact counts, and Snorlax itself is one of them.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per
from spirit.game.card_effects.passives_common import (is_in_active_spot,
                                                       no_retreat_passive,
                                                       opposing_active)
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    subtypes_for)


def is_team_plasma(pokemon) -> bool:
    return "Team Plasma" in subtypes_for(pokemon.archetype_id)


card = PokemonCardDef(
    guid="4850705b-adec-5a45-a1d2-a45fd9987589",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Team Plasma"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=101,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Block",
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon can't retreat.",
            passive=no_retreat_passive(
                lambda p, c: opposing_active(p, c) and is_in_active_spot(c)),
        ),
        Attack(
            title="Teamact",
            game_text="Does 30 damage times the number of Team Plasma Pokémon you have in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=30,
            effect=damage_per(count_in_play("mine", pred=is_team_plasma), 30),
        ),
    ],
)
