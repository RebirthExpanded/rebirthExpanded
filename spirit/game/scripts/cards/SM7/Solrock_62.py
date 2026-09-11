"""Solrock (SM - Celestial Storm 62/168 -- JP SM7b 029/050).

Basic Psychic Pokemon. HP 90, weakness Psychic x2, retreat 1.

  Ability  Sunbeam  The maximum HP of each of your Lunatone in play is 130.
  Scorching Light  [C]  Flip a coin. If heads, your opponent's Active
                        Pokemon is now Paralyzed. If tails, your
                        opponent's Active Pokemon is now Burned.
"""

from spirit.game.attributes import (AttrID, PokemonStage, PokemonTypes,
                                    Rarities, SpecialConditions)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, def_for
from spirit.game.session.passives import Passive


class SunbeamPassive(Passive):
    stacking_key = "sunbeam"

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        if getattr(def_for(pokemon.archetype_id), "display_name", "") != "Lunatone":
            return 0
        printed = pokemon.attribute_originals.get(AttrID.HP.value,
                                                  pokemon.get_attribute(AttrID.HP, 0))
        return max(0, 130 - printed)


card = PokemonCardDef(
    guid="bb909bbd-c26d-5e99-b633-2e037318f7f8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=338,
    abilities=[
        Ability(title="Sunbeam",
                game_text="The maximum HP of each of your Lunatone in play is 130.",
                passive=SunbeamPassive()),
        Attack(title="Scorching Light",
               game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed. If tails, your opponent's Active Pokémon is now Burned.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=condition_attack(SpecialConditions.PARALYZED, flip=True,
                                       tails_conditions=(SpecialConditions.BURNED,))),
    ],
)
