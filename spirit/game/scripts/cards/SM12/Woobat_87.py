"""Woobat (SM - Cosmic Eclipse 87/236 -- JP SM12 029/098).

Basic Psychic Pokemon. HP 60, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Nasal Suction  [C]  The Defending Pokemon can't retreat during your
                      opponent's next turn.
  Air Cutter  [P] 30  Flip a coin. If tails, this attack does nothing.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="2d95c34a-7cc7-590f-bbf5-3fa379ea479f",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=527,
    abilities=[
        Attack(title="Nasal Suction",
               game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
               cost={PokemonTypes.COLORLESS: 1}, damage=0,
               effect=condition_attack(no_retreat=True)),
        Attack(title="Air Cutter", game_text="Flip a coin. If tails, this attack does nothing.",
               cost={PokemonTypes.PSYCHIC: 1}, damage=30, effect=flip_or_nothing()),
    ],
)
