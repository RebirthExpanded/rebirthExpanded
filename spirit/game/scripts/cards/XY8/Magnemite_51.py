"""Magnemite (XY - BREAKthrough 51/162 -- JP XY8-Bb 021/059).

Basic Lightning Pokemon. HP 60, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Ability  Sparkling Induction  As long as this Pokemon is your Active
                                Pokemon, its Retreat Cost is [C] less for
                                each Magnemite on your Bench.
  Lightning Ball  [CC] 20

"Each Magnemite on your Bench" is by NAME, so any Magnemite print counts,
and the reduction floors at 0 like every other retreat discount.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_magnemite(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Magnemite"


class SparklingInductionPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or not is_in_active_spot(pokemon):
            return cost
        bench = board.find_player_area(pokemon.owning_player_id, "bench")
        benched = sum(1 for p in (bench.children if bench else [])
                      if _is_magnemite(p))
        return cost - benched


card = PokemonCardDef(
    guid="420f6086-5bb5-5975-bf64-c65fc4cfb70a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Ability(
            title="Sparkling Induction",
            game_text="As long as this Pokémon is your Active Pokémon, its Retreat Cost is [C] less for each Magnemite on your Bench.",
            passive=SparklingInductionPassive(),
        ),
        Attack(
            title="Lightning Ball",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
