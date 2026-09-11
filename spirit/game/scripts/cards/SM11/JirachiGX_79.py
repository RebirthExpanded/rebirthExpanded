"""Jirachi-GX (SM - Unified Minds 79/236 -- JP SM-P promo).

Basic Psychic Pokemon-GX. HP 160, weakness Psychic x2, retreat 1.

  Ability  Psychic Zone  Don't apply [P] Weakness when Pokemon (both yours
                         and your opponent's) take damage from attacks.
  Star Search     [P]        Search your deck for an Energy card and attach
                             it to 1 of your [P] Pokemon. Then, shuffle your
                             deck.
  Star Shield-GX  [PPP] 100  Prevent all effects of attacks, including
                             damage, done to this Pokemon during your
                             opponent's next turn.

Psychic Zone turns off ONE Weakness type for everyone, which is narrower
than the "has no Weakness" passives the pool already had: the shield reads
the DEFENDER's Weakness types and only steps in when [P] is what would
apply, so a Psychic Pokemon still takes double from a Darkness attacker
that it is also weak to.

"Take damage from attacks" is the only window -- damage counters placed by
an effect never looked at Weakness in the first place.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef)
from spirit.game.session.effects import is_energy_card, is_pokemon_of_type
from spirit.game.session.passives import Passive


class PsychicZonePassive(Passive):
    """No [P] Weakness for anyone taking attack damage."""

    def modify_weakness(self, calc, carrier):
        # The [P] Weakness specifically, not the Pokemon's Weakness as a
        # whole: strike Psychic off the list and leave any other type on it.
        calc.weak_types = [t for t in (calc.weak_types or [])
                           if t != PokemonTypes.PSYCHIC.value]


card = PokemonCardDef(
    guid="7078463f-294a-5a7e-ba00-13b884fe7a5c",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiGX.Name",
    display_name="Jirachi-GX",
    searchable_by=["Jirachi-GX", "Basic", "GX", "JirachiGX"],
    subtypes=["Basic", "GX"],
    collector_number=79,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Psychic Zone",
            game_text="Don't apply Psychic Weakness when Pokémon (both yours and your opponent's) take damage from attacks.",
            passive=PsychicZonePassive(),
        ),
        Attack(
            title="Star Search",
            game_text="Search your deck for an Energy card and attach it to 1 of your Psychic Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_attach_energy(
                predicate=is_energy_card, count=1,
                target_pred=lambda p: is_pokemon_of_type(
                    p, PokemonTypes.PSYCHIC)),
        ),
        Attack(
            title="Star Shield-GX",
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            gx=True,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)
