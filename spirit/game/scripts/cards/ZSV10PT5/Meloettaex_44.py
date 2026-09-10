"""Meloetta ex (SV - Black Bolt 044/086 -- JP SV11B 047/086).

Basic Psychic Pokemon ex. HP 200, weakness Darkness x2, resistance
Fighting -30, retreat 1, regulation mark I.

  Ability  Debut Performance  If you go first, this Pokemon can use attacks
                              during your first turn.

  Echoed Voice  [P] 30  During your next turn, this Pokemon's Echoed Voice
                        attack does 80 more damage (before applying Weakness
                        and Resistance).

The pool already had the per-attack form of the first-turn permission --
Fast Raid and Watch Over carry usable_first_turn, which lifts the ban for
that one attack. Debut Performance lifts it for the whole Pokemon, and a
continuous Ability is a passive, so this adds the passive-side hook
(attacks_first_turn) that legal_actions asks before applying the turn-1
gate. Either route now opens the same door.

It is the Ability of THIS Pokemon, so it only speaks for its own carrier:
a Benched Meloetta ex does not let the Active attack on turn 1.

Echoed Voice is Fullmetal Impact's rider with a title on it -- the +80 is
promised to Echoed Voice specifically, not to whatever this Pokemon
attacks with next turn -- which is exactly what boost_own_next_turn's
attack_title argument already does. Two Meloetta ex do not share the
promise: the rider is keyed to the attacking entity.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn
from spirit.game.session.passives import Passive, carrier_pokemon

ECHOED_VOICE = "Echoed Voice"


class DebutPerformancePassive(Passive):
    """The carrier may attack on the going-first player's first turn."""

    def attacks_first_turn(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon


card = PokemonCardDef(
    guid="54199c58-579b-5c9d-8f9a-cd1d9c137863",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloettaex.Name",
    display_name="Meloetta ex",
    searchable_by=["Meloetta ex", "Basic", "ex", "Meloettaex"],
    subtypes=["Basic", "ex"],
    collector_number=44,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=648,
    abilities=[
        Ability(
            title="Debut Performance",
            game_text="If you go first, this Pokémon can use attacks during your first turn.",
            passive=DebutPerformancePassive(),
        ),
        Attack(
            title=ECHOED_VOICE,
            game_text="During your next turn, this Pokémon's Echoed Voice attack does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=boost_own_next_turn(80, attack_title=ECHOED_VOICE),
        ),
    ],
)
